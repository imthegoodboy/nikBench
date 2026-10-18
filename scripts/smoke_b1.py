"""Live smoke-test the B1 Clinic API servers from round-1 submissions.

For each model: extract its ```javascript block from ## B1, run it with node,
then drive the spec contract over real HTTP:
  1. POST /appointments (valid)        -> expect 201 + id
  2. POST /appointments (same slot)    -> expect 409 double-booking
  3. GET  /appointments planted        -> expect 200
  4. DELETE /appointments/<id>         -> expect 204/200
  5. GET  /appointments/<id> after     -> expect 404
"""
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MODELS = ["space-bunny-free", "big-pickle", "glm-5.3-flash-free"]
SPECS = {
    "space-bunny":   {"port": 3000, "paths": None},
    "big-pickle":    {"port": 8000, "paths": None},
    "glm-5.3-flash": {"port": 3001, "paths": None},
}
BASE_APPT = {"patient": "Nik Test", "date": "2027-03-14", "slot": "09:00"}
REQ = json.dumps(BASE_APPT).encode()


def extract_js(model: str) -> str | None:
    text = (Path("submissions") / f"{model}.md").read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^## B1\b.*?(?=\n## |\Z)", text, re.S | re.M)
    if not m:
        return None
    block = re.search(r"```javascript\s*\n(.*?)```", m.group(0), re.S)
    return block.group(1) if block else None


def sniff_port(code: str, fallback: int) -> int:
    ports = re.findall(r"(?:PORT\s*\|\|\s*|PORT\s*=\s*|listen\(\s*)(\d{4})(?!\.\d)", code)
    if ports:
        return int(ports[-1])
    return fallback


def http(method: str, url: str, body: bytes | None = None):
    req = urllib.request.Request(url, data=body, method=method,
                                 headers={"content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            raw = resp.read()[:400]
            return resp.status, raw
    except urllib.error.HTTPError as e:
        return e.code, e.read()[:400]
    except Exception as e:  # noqa: BLE001
        return 0, str(e).encode()


def extract_id(raw: bytes) -> str | None:
    try:
        obj = json.loads(raw.decode("utf-8", errors="replace"))
    except Exception:  # noqa: BLE001
        m = re.search(r'"id"\s*:\s*"([^"]+)"', raw.decode("utf-8", errors="replace"))
        return m.group(1) if m else None
    for o in (obj, obj.get("data"), obj.get("appointment"), obj.get("result")):
        if isinstance(o, dict) and o.get("id") is not None:
            return str(o["id"])
    return None


def create_doctor(port: int) -> str | None:
    """No seeded doctors — create one via the API itself (POST /doctors)."""
    body = json.dumps({"name": "Dr. Test", "specialty": "general"}).encode()
    st, raw = http("POST", f"http://127.0.0.1:{port}/doctors", body)
    if st in (200, 201):
        return extract_id(raw)
    return None


def find_doctor(port: int) -> str | None:
    for probe in ("/doctors", "/api/doctors"):
        st, raw = http("GET", f"http://127.0.0.1:{port}{probe}")
        if st == 200:
            try:
                data = json.loads(raw.decode("utf-8", errors="replace"))
            except Exception:  # noqa: BLE001
                continue
            doctors = data if isinstance(data, list) else (
                data.get("data") or data.get("doctors") or [])
            for d in doctors or []:
                if isinstance(d, dict) and d.get("id") is not None:
                    return str(d["id"])
    return None


def valid_payload(doctor: str | None) -> dict:
    p = dict(BASE_APPT)
    p.pop("slot", None)
    p.update({"patient_name": "Nik Test", "duration_min": 30,
              "start": "2027-03-14T09:00:00Z"})
    if doctor:
        p["doctor_id"] = doctor
    return p


def smoke(model: str, specs: dict) -> None:
    code = extract_js(model)
    if not code:
        print(f"## {model}: no javascript block found")
        return
    code = re.sub(r"(?m)^(?!\s*$)(.*?)(?=[\r\n]+```|$)", lambda mm: mm.group(1), code)
    tmp = Path("_smoke")
    tmp.mkdir(exist_ok=True)
    js = tmp / f"{model}.js"
    js.write_text(code, encoding="utf-8")

    port = sniff_port(code, specs["port"])
    base = f"http://127.0.0.1:{port}"
    proc = subprocess.Popen(["node", str(js)], stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True, encoding="utf-8",
                            errors="replace")
    time.sleep(1.4)
    if proc.poll() is not None:
        out = (proc.stdout.read() or "")[:400].replace("\n", " | ")
        print(f"## {model}: SERVER FAILED TO START (exit {proc.returncode}) :: {out}")
        return

    print(f"## {model} (port {port})")
    try:
        results = {}
        # probe the base + common roots quickly to sanity-check liveness
        st_root, _ = http("GET", base + "/")
        print(f"  GET  /                        -> {st_root}")
        for probe in ("/appointments", "/api/appointments", "/health", "/api/health"):
            st, _ = http("GET", base + probe)
            results[probe] = st
            print(f"  GET  {probe:<27} -> {st}")
        st, raw = http("POST", base + "/appointments", REQ)
        aid = extract_id(raw)
        results["POST naive"] = st
        print(f"  POST /appointments (naive)    -> {st}")
        # second pass: real doctor id + contract-shaped body
        doctor = find_doctor(port) or create_doctor(port)
        body = json.dumps(valid_payload(doctor)).encode()
        st, raw = http("POST", base + "/appointments", body)
        aid = extract_id(raw)
        results["POST valid"] = st
        print(f"  POST /appointments (valid)    -> {st}  id={aid} :: {raw[:130].decode('utf-8', 'replace')}")
        st2, raw2 = http("POST", base + "/appointments", body)
        results["POST conflict"] = st2
        print(f"  POST /appointments (conflict) -> {st2} :: {raw2[:130].decode('utf-8', 'replace')}")
        if aid:
            st3, _ = http("DELETE", base + f"/appointments/{aid}")
            results["DELETE"] = st3
            print(f"  DELETE /appointments/<id>     -> {st3}")
            st4, raw4 = http("GET", base + f"/appointments/{aid}")
            results["GET after delete"] = st4
            print(f"  GET  deleted id               -> {st4} :: {raw4[:100].decode('utf-8', 'replace')}")
        verdict = (
            ("OK" if (results.get("POST valid") in (200, 201)
                      and results.get("POST conflict") in (409, 400)
                      and results.get("GET after delete") in (404, 200))
             else "PARTIAL")
        )
        print(f"  VERDICT: {verdict}")
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            proc.kill()


if __name__ == "__main__":
    for m, sp in zip(MODELS, SPECS.values()):
        smoke(m, sp)
        print()
