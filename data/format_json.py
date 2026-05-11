import json
from pathlib import Path


def load_json_of_list(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise TypeError("JSONの最上位はlistである必要がある")

    for item in data:
        if not isinstance(item, dict):
            raise TypeError("JSONの各要素はdictである必要がある")

    return data


def dump_company_by_chunk(
    companies: list[dict],
    out_dir: Path,
    basis: str = "company",
    size: int = 10,
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    for index, start in enumerate(range(0, len(companies), size), start=1):
        chunk = companies[start : start + size]
        path = out_dir / f"{basis}_{index:02d}.json"

        with path.open("w", encoding="utf-8") as f:
            json.dump(chunk, f, ensure_ascii=False, indent=4)


def dump_names_of_all(
    companies: list[dict],
    out_dir: Path,
    filename: str = "names.json",
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    names = []
    for company in companies:
        names.append(company.get("name", "ERROR"))
    filepath = out_dir / filename

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(names, f, ensure_ascii=False, indent=4)

    return


if __name__ == "__main__":
    from flaskdotcom.utils.root import find_project_root

    root = find_project_root()

    data_dir = root / "data"
    src = data_dir / "all.json"

    companies = load_json_of_list(src)
    dump_company_by_chunk(companies, data_dir)
    dump_names_of_all(companies, data_dir)
