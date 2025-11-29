from src.models.filter import Filter
from src.models.filter_type import FilterType


class FilterUtils:
    @staticmethod
    def find_filter(filters: list[Filter], key: str, filter_type: FilterType) -> Filter | None:
        for filter in filters:
            if filter.key == key and filter.filter_type == filter_type:
                return filter
        

        return None
    

    @staticmethod
    def remove_filter(filters: list[Filter], key: str, filter_type: FilterType) -> list[Filter]:
        return [filter for filter in filters if filter.key != key or filter.filter_type != filter_type]