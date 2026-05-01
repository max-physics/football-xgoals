import json
from pathlib import Path

def load_competitions():
    BASE = Path("open-data/data/")
    with open(BASE / "competitions.json") as f:
        competitions = json.load(f)
    return competitions