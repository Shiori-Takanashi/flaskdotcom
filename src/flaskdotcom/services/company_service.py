from dataclasses import dataclass, field

from ..infrastracture.load_json import get_data_from_json


@dataclass
class Company:
    index: int
    name: str
    market: str
    category: str
    lead: str
    sales: float
    profit: float
    features: list[str]


@dataclass
class Pagination:
    requested_page: int
    per_page: int
    total_items: int
    companies: list[Company] = field(default_factory=list)

    @property
    def total_pages(self) -> int:
        if self.total_items == 0:
            return 0
        return (self.total_items + self.per_page - 1) // self.per_page

    @property
    def current_page(self) -> int:
        if self.requested_page < 1:
            return 1
        if self.total_pages > 0 and self.requested_page > self.total_pages:
            return self.total_pages
        return self.requested_page

    @property
    def has_prev(self) -> bool:
        return self.current_page > 1

    @property
    def has_next(self) -> bool:
        return self.current_page < self.total_pages


def calculate_index(requested_page: int, per_page: int) -> tuple[int, int]:
    prev_items = (requested_page - 1) * per_page
    return prev_items + 1, prev_items + per_page


def get_pagination(requested_page: int, per_page: int) -> Pagination:
    """ページネーションの構築とデータ取得を調整するサービス関数"""
    start, end = calculate_index(requested_page, per_page)
    all_items = get_data_from_json()
    return Pagination(
        requested_page, per_page, len(all_items), all_items[start - 1 : end]
    )


if __name__ == "__main__":
    pagination = get_pagination(2, 10)
    print(pagination.__dict__)
