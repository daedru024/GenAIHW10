"""Check 1: every claim line in the Wiki must cite a source ID, and every ID must exist in sources.md."""
import re, sys, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
known = set(re.findall(r"^\| (S\d+) \|", (root / "sources.md").read_text(), re.M))
retired = {"S5"}
files = [*root.glob("concepts/*.md"), *root.glob("hall-types/*.md"), *root.glob("halls/*.md"), root / "conflicts.md"]

problems = 0
for f in files:
    for n, line in enumerate(f.read_text().splitlines(), 1):
        s = line.strip()
        is_claim = (s.startswith("- ") or (s.startswith("|") and not set(s) <= set("|-: "))
                    or s.startswith("**In one sentence"))
        if not is_claim or s.startswith("| Type |") or s.startswith("| Context |"):
            continue
        ids = set(re.findall(r"\[(S\d+)\]", s))
        skip = s.startswith("- S5") or "See also" in s or re.match(r"- (Seat counts|Some odd)", s)
        if not ids and not skip:
            print(f"NO SOURCE  {f.relative_to(root)}:{n}: {s[:80]}"); problems += 1
        for i in ids:
            if i not in known:
                print(f"UNKNOWN ID {f.relative_to(root)}:{n}: {i}"); problems += 1
            if i in retired:
                print(f"RETIRED ID {f.relative_to(root)}:{n}: {i}"); problems += 1
print("OK: all claims cited" if not problems else f"{problems} problem(s)")
sys.exit(1 if problems else 0)
