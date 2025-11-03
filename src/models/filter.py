from src.models.base_model import BaseModel
from src.models.filter_type import FilterType


class Filter(BaseModel):
    """
    Represents a filtering condition used for data queries.

    Attributes:
        key (str): The field name to apply the filter to.
        value (str): The value to filter by.
        filter_type (FilterType): The type of comparison (e.g., EQUALS, LIKE, BETWEEN).
    """

    _key: str
    _value: str
    _filter_type: FilterType

    def __init__(self, key: str, value: str, filter_type: FilterType):
        """
        Initializes a new filter instance.

        Args:
            key (str): The name of the field to filter.
            value (str): The value to match.
            filter_type (FilterType): The comparison operation type.
        """
        super().__init__()
        self._key = key
        self._value = value
        self._filter_type = filter_type

    @property
    def key(self) -> str:
        """Returns the filter key (field name)."""
        return self._key

    @property
    def value(self) -> str:
        """Returns the filter value."""
        return self._value

    @property
    def filter_type(self) -> FilterType:
        """Returns the filter type (comparison method)."""
        return self._filter_type

    @key.setter
    def key(self, value: str) -> None:
        """Sets a new key for the filter."""
        self._key = value
