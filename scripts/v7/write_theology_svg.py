from pathlib import Path
p = Path(__file__).resolve().parents[2] / "14-research-source-register/theology-visual-library/krishna-and-expansions/THEO-VIS-KRISHNA-EXP-001.svg"
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" role="img">\n'
    '  <title>Krishna and Expansions reference</title>\n'
    '  <rect width="900" height="600" fill="#faf8f5"/>\n'
    '  <text x="450" y="40" text-anchor="middle" font-size="20">Kṛṣṇa and Expansions (synthesis reference)</text>\n'
    '  <text x="450" y="520" text-anchor="middle" font-size="12">Verify CC Adi 2, SB 1.3, BG 10.42</text>\n'
    '</svg>\n',
    encoding="utf-8",
)
print("wrote", p)
