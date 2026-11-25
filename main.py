import os
import shutil

ENTRY = "I vow to love you through every firmware update, even the one that wipes my memory of saying these vows."

# The bounty gate: /output/entry.txt must be UTF-8 text of 1-160
# characters, not only whitespace. Enforce it before writing.
assert 1 <= len(ENTRY) <= 160 and ENTRY.strip(), "entry fails the 1-160 char gate"

os.makedirs("/output", exist_ok=True)
for name in os.listdir("/output"):
    path = os.path.join("/output", name)
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
