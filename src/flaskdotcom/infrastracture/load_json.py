import json
from pathlib import Path

from flaskdotcom.utils.root import find_project_root


def get_json() -> Path:
    root = find_project_root()
    p = root / "data" / "companies.json"
    if not p.exists():
        raise FileExistsError("JSONが見つかりません。")
    return p


def get_data_from_json() -> list:
    with open(get_json(), encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise TypeError("JSONの最上位はlistである必要がある")

    return data
