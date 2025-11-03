from typing import TypeVar, List

from src.store.filter_type_processor import (
    LikeFilterTypeProcessor,
    EqualsFilterTypeProcessor,
    BetweenFilterTypeProcessor
)
from src.models.filter import Filter
from src.models.filter_type import FilterType

T = TypeVar('T')


class ListFilterer:
    """
    Applies a set of filters to a list of items using corresponding filter processors.
    """

    # Mapping of FilterType enum to corresponding processor instances
    __filterers_map = {
        FilterType.LIKE: LikeFilterTypeProcessor(),
        FilterType.EQUALS: EqualsFilterTypeProcessor(),
        FilterType.BETWEEN: BetweenFilterTypeProcessor()
    }

    @staticmethod
    def apply_filters(items: List[T], filters: List[Filter]) -> List[T]:
        """
        Filters a list of items based on a list of Filter objects.

        Args:
            items (List[T]): List of items to filter.
            filters (List[Filter]): List of filters to apply.

        Returns:
            List[T]: Filtered list of items that satisfy all filters.
        """
        return [
            item for item in items
            if all(
                ListFilterer.__filterers_map[filter.filter_type].process(item, filter)
                for filter in filters
            )
        ]
