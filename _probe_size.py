# -*- coding: utf-8 -*-
from pathlib import Path

code = Path("_gen_gold_packs.py").read_text(encoding="utf-8")
code = code.replace('print("C2-W5 defined", flush=True)', "")
ns = {}
exec(compile(code, "_gen_gold_packs.py", "exec"), ns)
w = ns["WEEKS"][0]
main = ns["render_main"](w)
print("C2-W5 MAIN chars:", len(main))
print("speaking_script chars:", len(w["speaking_script"]))
# Estimate needed expansion
print("Need +", max(0, 15000 - len(main)), "chars in MAIN")
