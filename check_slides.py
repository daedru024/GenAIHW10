"""Check 2: every slide must name existing Wiki pages and known, non-retired source IDs."""
import re, sys, pathlib

wiki = pathlib.Path(__file__).resolve().parent.parent
deck = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else wiki.parent / "slides" / "index.html")
known = set(re.findall(r"^\| (S\d+) \|", (wiki / "sources.md").read_text(), re.M))
pages = {p.stem for p in wiki.rglob("*.md")}
slides = re.findall(r'<section class="slide[^"]*" data-wiki="([^"]*)" data-sources="([^"]*)"', deck.read_text())
bad = 0
for n, (w, s) in enumerate(slides, 1):
    for page in [x.strip() for x in w.split(",")]:
        if page not in pages: print(f"slide {n}: missing Wiki page '{page}'"); bad += 1
    for sid in [x.strip() for x in s.split(",")]:
        if sid not in known: print(f"slide {n}: unknown source {sid}"); bad += 1
        if sid == "S5": print(f"slide {n}: retired source S5"); bad += 1
print(f"{len(slides)} slides checked;", "OK" if not bad else f"{bad} problem(s)")
sys.exit(1 if bad else 0)
