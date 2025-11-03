from src.exceptions.validation import ArgumentException
from src.models.base_model import BaseModel
from src.models.measurement_unit import MeasurementUnit


class MeasuredValue(BaseModel):
    """
    Represents a measurable quantity with an associated measurement unit.

    Attributes:
        value (float): The numeric amount of the measurement.
        unit (MeasurementUnit): The unit associated with the value (e.g., grams, liters).
    """

    _value: float = 0
    _unit: MeasurementUnit = None

    def __init__(self, value: float = None, unit: MeasurementUnit = None):
        """
        Initializes a MeasuredValue instance.

        Args:
            value (float, optional): The numeric value of the measurement.
            unit (MeasurementUnit, optional): The measurement unit.
        """
        super().__init__()
        self.value = value
        self.unit = unit

    def to_root(self) -> 'MeasuredValue':
        """
        Converts the current value to its root (base) unit recursively.

        Returns:
            MeasuredValue: A new instance converted to the base unit.
        """
        if self.unit.base_unit is None:
            return self
        return MeasuredValue(self.converted_value, self.unit.base_unit).to_root()

    @property
    def value(self) -> float:
        """Returns the measured numeric value."""
        return self._value

    @value.setter
    def value(self, new_value: float) -> None:
        """
        Sets the measured value.

        Raises:
            ArgumentException: If the value is not a number.
        """
        if new_value is not None and not isinstance(new_value, (int, float)):
            raise ArgumentException("Value must be numeric.")
        self._value = new_value

    @property
    def unit(self) -> MeasurementUnit:
        """Returns the measurement unit."""
        return self._unit

    @unit.setter
    def unit(self, new_unit: MeasurementUnit) -> None:
        """
        Sets the measurement unit.

        Raises:
            ArgumentException: If the unit is not a MeasurementUnit instance.
        """
        if new_unit is not None and not isinstance(new_unit, MeasurementUnit):
            raise ArgumentException("Unit must be an instance of MeasurementUnit.")
        self._unit = new_unit
