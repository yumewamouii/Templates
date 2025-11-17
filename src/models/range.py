import datetime
from src.exceptions.validation import ArgumentException


class RangeModel:
    """
    Represents a range between two comparable values (numbers or datetimes).

    Attributes:
        from_value (datetime | float | int): The start of the range.
        to_value (datetime | float | int): The end of the range.
    """

    _from_value: datetime.datetime | float | int
    _to_value: datetime.datetime | float | int

    def __init__(self, from_value, to_value):
        """
        Initializes a RangeModel instance.

        Args:
            from_value (datetime | float | int): Start of the range.
            to_value (datetime | float | int): End of the range.

        Raises:
            ArgumentException: If either value is of an unsupported type.
        """
        self.from_value = from_value
        self.to_value = to_value

    @property
    def from_value(self):
        """Returns the start of the range."""
        return self._from_value

    @from_value.setter
    def from_value(self, value):
        """
        Sets the start of the range.

        Raises:
            ArgumentException: If value is not datetime, float, or int.
        """
        if not isinstance(value, (datetime.datetime, float, int)):
            raise ArgumentException((datetime.datetime, float, int), type(value))
        self._from_value = value

    @property
    def to_value(self):
        """Returns the end of the range."""
        return self._to_value

    @to_value.setter
    def to_value(self, value):
        """
        Sets the end of the range.

        Raises:
            ArgumentException: If value is not datetime, float, or int.
        """
        if not isinstance(value, (datetime.datetime, float, int)):
            raise ArgumentException((datetime.datetime, float, int), type(value))
        self._to_value = value
