from pathlib import Path


def find_project_root(
    path: Path | None = None, depth: int = 0, limit: int = 12
) -> Path:
    DIRS = [".git"]
    FILES = ["pyproject.toml"]

    if path is None:
        path = Path(__file__).resolve()

    if path.is_file():
        path = path.parent

    for d in DIRS:
        if (path / d).is_dir():
            return path

    for f in FILES:
        if (path / f).is_file():
            return path

    # 終了条件: 探索上限の深さに達した、またはファイルシステムのルートに到達した場合は例外を送出
    if depth >= limit or path == path.parent:
        raise FileNotFoundError(
            f"プロジェクトのルートディレクトリが見つかりませんでした。(探索開始パス: {path})"
        )

    return find_project_root(path.parent, depth + 1, limit)
