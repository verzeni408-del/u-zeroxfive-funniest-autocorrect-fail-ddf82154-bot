from pathlib import Path

ENTRY = "I texted Mom 'tell dead I said happy birthday.' He died in March, and she just replied 'I will.'"

assert 1 <= len(ENTRY) <= 199, "entry must be 1-199 characters"
assert "\n" not in ENTRY, "entry must be a single line"

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(ENTRY, encoding="utf-8")
