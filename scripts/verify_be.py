"""Live contract smoke-test for EVERY model's B1 Clinic API (v3.0 hard build).

Extracts each model's ```javascript block from its submission, boots it under
node, and drives the v3.0 spec over real HTTP: health + request IDs, idempotency
replay/conflict, ETag/If-Match (428/412), pagination cursors, audit log, the
overlap/priority rules, and the state machine. Reports a 0–100 score so the BE
pillar stops being 'mentally executed'.

Windows note: SIGTERM semantics are not portable, so graceful shutdown is a
static check on the source (SIGINT|SIGTERM handling) instead of a live signal.
"""
import argparse
import json as _json
import os
import re
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
import uuid
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


def free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def req(base, method, path, body=None, headers=None, timeout=5):
    """Return (status, headers_lower, json_obj_or_None, raw_bytes)."""
    hdrs = {"content-type": "application/json"}
    if headers:
        for k, v in headers.items():
            hdrs[k] = v
    data = body if isinstance(body, (bytes, type(None))) else body.encode()
    r = urllib.request.Request(base + path, data=data, method=method, headers=hdrs)
    try:
        with urllib.request.urlopen(r, timeout=timeout) as resp:
            raw = resp.read()
            h = {k.lower(): v for k, v in resp.headers.items()}
            try:
                obj = _json.loads(raw.decode("utf-8", errors="replace"))
            except Exception:  # noqa: BLE001
                obj = None
            return resp.status, h, obj, raw
    except urllib.error.HTTPError as e:
        raw = e.read()
        h = {k.lower(): v for k, v in e.headers.items()}
        try:
            obj = _json.loads(raw.decode("utf-8", errors="replace"))
        except Exception:  # noqa: BLE001
            obj = None
        return e.code, h, obj, raw
    except Exception as e:  # noqa: BLE001
        return 0, {}, None, str(e).encode()


def err_code(obj):
    if isinstance(obj, dict) and isinstance(obj.get("error"), dict):
        return str(obj["error"].get("code", ""))
    return ""


def extract_id(obj):
    for o in (obj, (obj or {}).get("data") if isinstance(obj, dict) else None):
        if isinstance(o, dict) and o.get("id") is not None:
            return str(o["id"])
    return None


def run_one(model: str) -> tuple[int, str]:
    code = extract_js(model)
    if not code:
        return 0, "NO-B1-SECTION"
    js = SMOKE / f"{model}.js"
    js.write_text(code, encoding="utf-8")
    port = free_port()
    env = dict(os.environ)
    env["PORT"] = str(port)
    proc = subprocess.Popen(["node", str(js)], stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True,
                            encoding="utf-8", errors="replace", env=env)
    base = f"http://127.0.0.1:{port}"
    # wait for boot; fall back to a sniffed hardcoded port if needed
    booted = False
    deadline = time.time() + 6
    while time.time() < deadline:
        if proc.poll() is not None:
            break
        st, _h, _o, _r = req(base, "GET", "/health", timeout=1)
        if st == 200:
            booted = True
            break
        time.sleep(0.25)
    if not booted:
        alt = sniff_port(code)
        if alt != port:
            base = f"http://127.0.0.1:{alt}"
            for _ in range(8):
                st, _h, _o, _r = req(base, "GET", "/health", timeout=1)
                if st == 200:
                    booted = True
                    break
                time.sleep(0.25)
    checks: list[tuple[str, bool]] = []

    def ok(name, cond):
        checks.append((name, bool(cond)))
        return bool(cond)

    if not booted:
        try:
            out = (proc.stdout.read() or "")[:160].replace("\n", " | ") if proc.poll() is not None else "timeout"
        except Exception:  # noqa: BLE001
            out = "?"
        proc.terminate()
        return 0, f"BOOT-FAIL ({out})"

    try:
        st, h, obj, _ = req(base, "GET", "/health")
        ok("health 200 + status ok", st == 200 and isinstance(obj, dict) and obj.get("status") == "ok")
        ok("health uptime_s int", isinstance(obj, dict) and isinstance(obj.get("uptime_s"), (int, float)))
        ok("X-Request-Id on success", bool(h.get("x-request-id")))
        rid = str(uuid.uuid4())
        st, h2, _, _ = req(base, "GET", "/health", headers={"X-Request-Id": rid})
        ok("X-Request-Id echo", h2.get("x-request-id") == rid)

        st, h3, obj3, _ = req(base, "GET", "/appointments/does-not-exist")
        ok("error envelope {code,message,request_id}",
           st == 404 and isinstance(obj3, dict)
           and err_code(obj3) == "APPOINTMENT_NOT_FOUND"
           and isinstance(obj3.get("error"), dict) and "request_id" in obj3["error"]
           and bool(h3.get("x-request-id")))

        # ---- doctors + idempotency
        doc_body = {"name": "Dr. Nik", "specialty": "general"}
        st, _, dobj, _ = req(base, "POST", "/doctors", _json.dumps(doc_body),
                             headers={"Idempotency-Key": "nb-doc-1"})
        doctor = extract_id(dobj)
        ok("POST /doctors 201", st == 201 and doctor is not None and doctor.startswith("dr_"))
        st2, _, dobj2, _ = req(base, "POST", "/doctors", _json.dumps(doc_body),
                               headers={"Idempotency-Key": "nb-doc-1"})
        ok("idempotent doctor replay", st2 in (200, 201) and extract_id(dobj2) == doctor)
        st3, _, dobj3, _ = req(base, "POST", "/doctors", _json.dumps({"name": "Dr. Other", "specialty": "derma"}),
                               headers={"Idempotency-Key": "nb-doc-1"})
        ok("idempotency conflict 409", st3 == 409 and err_code(dobj3) == "IDEMPOTENCY_CONFLICT")

        # ---- appointments
        def appt_body(start="2027-03-14T09:00:00Z", dur=30, patient="Nik T"):
            return {"doctor_id": doctor, "patient_name": patient, "start": start, "duration_min": dur}

        st, ah, aobj, _ = req(base, "POST", "/appointments", _json.dumps(appt_body()),
                              headers={"Idempotency-Key": "nb-appt-1", "X-Actor": "tester"})
        appt = extract_id(aobj)
        version = aobj.get("version") if isinstance(aobj, dict) else None
        ok("POST /appointments 201 + v1", st == 201 and appt is not None and appt.startswith("appt_") and version == 1)
        ok("ETag on create", bool(ah.get("etag")))
        st2, _, aobj2, _ = req(base, "POST", "/appointments", _json.dumps(appt_body()),
                               headers={"Idempotency-Key": "nb-appt-1"})
        ok("idempotent appointment replay", extract_id(aobj2) == appt)

        st, _, cobj, _ = req(base, "POST", "/appointments", _json.dumps(appt_body()))
        ok("overlap -> 409 SLOT_TAKEN", st == 409 and err_code(cobj) == "SLOT_TAKEN")
        st, _, tobj, _ = req(base, "POST", "/appointments", _json.dumps(appt_body(start="2027-03-14T09:30:00Z")))
        touch = extract_id(tobj)
        ok("touching booking allowed", st == 201 and touch is not None)
        st, _, nobj, _ = req(base, "POST", "/appointments",
                             _json.dumps({"doctor_id": "dr_nope", "patient_name": "X Z",
                                          "start": "2027-03-15T09:00:00Z", "duration_min": 30}))
        ok("unknown doctor 404", st == 404 and err_code(nobj) == "DOCTOR_NOT_FOUND")
        st, _, bobj, _ = req(base, "POST", "/appointments", b"{not json")
        ok("malformed JSON 400", st == 400 and err_code(bobj) == "INVALID_JSON")
        st, _, vobj, _ = req(base, "POST", "/appointments",
                             _json.dumps({"doctor_id": doctor, "patient_name": "A B",
                                          "start": "2027-03-15T10:00:00Z", "duration_min": 17}))
        ok("invalid field 422 VALIDATION_ERROR", st == 422 and err_code(vobj) == "VALIDATION_ERROR")

        st, _, lobj, _ = req(base, "GET", "/appointments?limit=1")
        has_shape = (st == 200 and isinstance(lobj, dict) and isinstance(lobj.get("data"), list)
                     and "next_cursor" in lobj)
        ok("pagination shape {data,next_cursor}", has_shape)
        first_id = lobj["data"][0]["id"] if has_shape and lobj["data"] else None
        cursor = lobj.get("next_cursor") if has_shape else None
        st, _, iobj, _ = req(base, "GET", "/appointments?limit=0")
        ok("invalid limit 422", st == 422)
        st, gh, gobj, _ = req(base, "GET", f"/appointments/{appt}")
        ok("GET one has ETag", st == 200 and bool(gh.get("etag")))

        st, _, pobj, _ = req(base, "PATCH", f"/appointments/{appt}",
                             _json.dumps({"status": "confirmed"}))
        ok("PATCH without If-Match 428", st == 428)
        st, _, pobj, _ = req(base, "PATCH", f"/appointments/{appt}",
                             _json.dumps({"status": "confirmed"}), headers={"If-Match": '"v99"'})
        ok("PATCH stale If-Match 412", st == 412)
        etag = gh.get("etag", '"v1"')
        st, ph, pobj, _ = req(base, "PATCH", f"/appointments/{appt}",
                              _json.dumps({"status": "confirmed"}), headers={"If-Match": etag})
        ok("PATCH valid -> confirmed", st in (200, 201) and isinstance(pobj, dict) and pobj.get("status") == "confirmed")
        ok("PATCH increments version", isinstance(pobj, dict) and (pobj.get("version") in (2, "2") or (ph.get("etag") and ph.get("etag") != etag)))

        st, _, caobj, _ = req(base, "POST", "/appointments",
                              _json.dumps(appt_body(start="2027-03-16T09:00:00Z", patient="Cancel Me")))
        cancel_id = extract_id(caobj)
        st, _, pcobj, _ = req(base, "PATCH", f"/appointments/{cancel_id}",
                              _json.dumps({"status": "cancelled"}), headers={"If-Match": '"v1"'})
        ok("PATCH cancel scheduled", st in (200, 201) and isinstance(pcobj, dict) and pcobj.get("status") == "cancelled")
        st, _, pcobj2, _ = req(base, "PATCH", f"/appointments/{cancel_id}",
                               _json.dumps({"status": "confirmed"}), headers={"If-Match": '"v2"'})
        ok("PATCH cancelled -> 409", st == 409 and err_code(pcobj2) == "APPOINTMENT_CANCELLED")
        st, _, _dobj, _ = req(base, "DELETE", f"/appointments/{cancel_id}")
        ok("DELETE cancelled -> 409", st == 409)
        st, _, _dob2, _ = req(base, "DELETE", f"/appointments/{touch}")
        ok("DELETE scheduled -> 204", st in (200, 204))
        st, _, _gobj, _ = req(base, "GET", f"/appointments/{touch}")
        ok("deleted appointment gone -> 404", st == 404)

        st, _, aulog, _ = req(base, "GET", "/audit?limit=200")
        events = aulog.get("data") if isinstance(aulog, dict) else None
        actions = [str(e.get("action", "")) for e in events] if isinstance(events, list) else []
        ok("audit log append-only events",
           st == 200 and isinstance(events, list) and len(events) >= 3
           and any("create" in a for a in actions) and any(("cancel" in a or "delete" in a) for a in actions))

        if cursor and first_id:
            st, _, p2, _ = req(base, "GET", f"/appointments?limit=1&cursor={cursor}")
            second_id = p2["data"][0]["id"] if isinstance(p2, dict) and p2.get("data") else None
            ok("cursor pages without duplicating", st == 200 and second_id is not None and second_id != first_id)
        else:
            ok("cursor pages without duplicating", False)

        ok("graceful shutdown handler (static)", bool(re.search(r"SIGINT|SIGTERM", code)))

        passed = sum(1 for _, c in checks if c)
        total = len(checks)
        failed = [n for n, c in checks if not c]
        score = round(passed / total * 100)
        detail = f"{passed}/{total}" + (f" — failed: {', '.join(failed[:8])}" if failed else " — all pass")
        return score, detail
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            proc.kill()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="print {model: live_score_0_100} JSON and exit")
    args = ap.parse_args()
    models = sorted(p.stem for p in (ROOT / "submissions").glob("*.md")
                    if p.name != "README.md")
    out = {}
    if args.json:
        for m in models:
            score, _detail = run_one(m)
            out[m] = score
        print(_json.dumps(out))
        for p in SMOKE.glob("*.js"):
            p.unlink(missing_ok=True)
        return
    print("BE live contract smoke v3.0 (idempotency / ETag / pagination / audit):")
    print(f"{'model':<32} {'score':>5}  detail")
    print("-" * 100)
    for m in models:
        score, detail = run_one(m)
        print(f"{m:<32} {score:>4}/100  {detail}")
    for p in SMOKE.glob("*.js"):
        p.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
