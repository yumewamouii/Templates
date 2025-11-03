import datetime

from src.mappers.basetype_mapper import BaseTypeMapper


class DatetimeMapper(BaseTypeMapper[datetime.datetime]):
    """
    Mapper for converting between datetime objects and Unix timestamps.
    """

    def from_model(self, obj: datetime.datetime) -> float:
        """
        Convert a datetime object to a Unix timestamp.
        
        Args:
            obj (datetime.datetime): Datetime object to convert.
        
        Returns:
            float: Unix timestamp representation of the given datetime.
        """
        return obj.timestamp()

    def to_model(self, data: float) -> datetime.datetime:
        """
        Convert a Unix timestamp back to a datetime object.
        
        Args:
            data (float): Unix timestamp to convert.
        
        Returns:
            datetime.datetime: Datetime object corresponding to the timestamp.
        """
        return datetime.datetime.fromtimestamp(data)
