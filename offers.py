import json
from pathlib import Path

offers_path = Path(_file_).parent.parent / "data" / "offers.json"

def get_offers_for_user(user: object) -> list:
    country = "RU"  # mock — заменить на IP геоопределение
    with open(offers_path, "r", encoding="utf-8") as f:
        all_offers = json.load(f)
    return [o for o in all_offers if country in o["countries"]]