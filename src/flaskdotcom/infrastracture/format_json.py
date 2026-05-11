import json

from flaskdotcom.utils.root import find_project_root


root = find_project_root(__file__)
origin = root / "data" / "company.json"

with open(origin, "w", encoding="utf-8") as f:
    data = json.load(f)

print(len(data))
