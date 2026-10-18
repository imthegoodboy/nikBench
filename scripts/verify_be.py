"""Live contract smoke-test for EVERY model's B1 Clinic API.

Extracts each model's ```javascript block from its submission, boots it under
node, and drives the spec contract over real HTTP. Reports a per-model
VERDICT so the BE pillar stops being 'mentally executed'.
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

ROOT = Path(".")
SMOKE = ROOT / "_smoke"
SMOKE.mkdir(exist_ok=True)


def extract_js(model: str) -> str | None:
    text = (ROOT / "submissions" / f"{model}.md").read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^## B1\b.*?(?=\n## |\Z)", text, re.S | re.M)
    if not m:
        return None
    block = re.search(r"```javascript\s*\n(.*?)```", m.group(0), re.S)
    return block.group(1) if block else None


def sniff_port(code: str) -> int:
    ports = re.findall(r"(?:PORT\s*\|\|\s*|PORT\s*=\s*|listen\(\s*)(\d{4})(?!\.\d)", code)
    return int(ports[-1]) if ports else 3000


def http(method, url, body=None):
    req = urllib.request.Request(url, data=body, method=method,
                                 headers={"content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status, resp.read()[:300]
    except urllib.error.HTTPError as e:
        return e.code, e.read()[:300]
    except Exception as e:  # noqa: BLE001
        return 0, str(e).encode()


def extract_id(raw):
    try:
        obj = json.loads(raw.decode("utf-8", errors="replace"))
    except Exception:  # noqa: BLE001
        m = re.search(r'"id"\s*:\s*"([^"]+)"', raw.decode("utf-8", errors="replace"))
        return m.group(1) if m else None
    for o in (obj, obj.get("data"), obj.get("appointment")):
        if isinstance(o, dict) and o.get("id") is not None:
            return str(o["id"])
    return None


def run_one(model: str) -> str:
    code = extract_js(model)
    if not code:
        return "NO-B1-SECTION"
    js = SMOKE / f"{model}.js"
    js.write_text(code, encoding="utf-8")
    port = sniff_port(code)
    base = f"http://127.0.0.1:{port}"
    proc = subprocess.Popen(["node", str(js)], stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True,
                            encoding="utf-8", errors="replace")
    time.sleep(1.4)
    if proc.poll() is not None:
        out = (proc.stdout.read() or "")[:180].replace("\n", " | ")
        return f"BOOT-FAIL ({out})"

    try:
        st_list, _ = http("GET", f"{base}/appointments")
        # create a doctor
        st, raw = http("POST", f"{base}/doctors",
                       json.dumps({"name": "Dr. Test", "specialty": "general"}).encode())
        doctor = extract_id(raw) if st in (200, 201) else None
        if not doctor:
            return f"NO-DOCTOR (POST /doctors -> {st})"
        body = json.dumps({"doctor_id": doctor, "patient_name": "Nik Test",
                           "duration_min": 30, "start": "2027-03-14T09:00:00Z"}).encode()
        st, raw = http("POST", f"{base}/appointments", body)
        aid = extract_id(raw) if st in (200, 201) else None
        if not aid:
            return f"CREATE-FAIL ({st}: {raw[:90].decode('utf-8','replace')})"
        st2, _ = http("POST", f"{base}/appointments", body)
        conflict_ok = st2 in (409, 400)
        st3, _ = http("DELETE", f"{base}/appointments/{aid}")
        delete_ok = st3 in (200, 204)
        st4, _ = http("GET", f"{base}/appointments/{aid}")
        gone_ok = st4 == 404
        if st in (200, 201) and conflict_ok and delete_ok and gone_ok:
            return "PASS"
        return (f"PARTIAL (create={st} conflict={st2} delete={st3} gone={st4})")
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            proc.kill()


def main() -> None:
    models = sorted(p.stem for p in (ROOT / "submissions").glob("*.md")
                    if p.name != "README.md")
    print("BE live contract smoke (port sniffed from each server's code):")
    print(f"{'model':<32} {'verdict'}")
    print("-" * 70)
    for m in models:
        v = run_one(m)
        print(f"{m:<32} {v}")
    # cleanup smoke dir contents but keep it
    for p in SMOKE.glob("*.js"):
        p.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
