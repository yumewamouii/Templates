from abc import ABC, abstractmethod
from typing import TypeVar

from src.mappers.absolute_mapper import AbsoluteMapper
from src.models.base_model import BaseModel
from src.models.filter import Filter
from src.models.range import RangeModel

T = TypeVar('T', bound=BaseModel)


class FilterTypeProcessor(ABC):
    """
    Base class for processing filters on models.
    Subclasses implement specific filter logic.
    """

    def process(self, item: T, filter: Filter) -> bool:
        """
        Applies the filter to a given item.

        Args:
            item (T): The model instance to filter.
            filter (Filter): The filter specification.

        Returns:
            bool: True if the item passes the filter, False otherwise.
        """
        item_dict = AbsoluteMapper.to_dict(item)
        keys_array = filter.key.split('.')
        inner_value = item_dict
        for key in keys_array:
            inner_value = inner_value.get(key, None)
            if inner_value is None:
                return False

        return self._process_internal(str(inner_value).lower(), str(filter.value).lower())

    @abstractmethod
    def _process_internal(self, value: str, waited_value: str) -> bool:
        """
        Internal method to compare a value to the filter criteria.

        Must be implemented by subclasses.

        Args:
            value (str): The stringified value from the model.
            waited_value (str): The stringified expected value.

        Returns:
            bool: Result of comparison.
        """
        raise NotImplementedError()


class LikeFilterTypeProcessor(FilterTypeProcessor):
    """Filter processor for substring matching (LIKE)."""

    def _process_internal(self, value: str, waited_value: str) -> bool:
        return waited_value in value


class EqualsFilterTypeProcessor(FilterTypeProcessor):
    """Filter processor for equality matching (EQUALS)."""

    def _process_internal(self, value: str, waited_value: str) -> bool:
        return value == waited_value


class BetweenFilterTypeProcessor(FilterTypeProcessor):
    """Filter processor for range checks (BETWEEN)."""

    def _process_internal(self, value, waited_value: RangeModel) -> bool:
        # Here, value should ideally be comparable (int, float, datetime)
        return waited_value.from_value <= value < waited_value.to_value
