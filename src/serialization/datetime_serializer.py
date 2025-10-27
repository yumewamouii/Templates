from typing import Any
from datetime import datetime


from src.serialization.base_serializer import BaseSerializer


from src.exceptions.validation import ArgumentException


class DatetimeSerializer(BaseSerializer):
    def serialize(self, obj: Any) -> dict[str, Any]:
        if not isinstance(obj, datetime):
            raise ArgumentException(f'Excepted datetime. Got {type(obj).__name__}')
        

        return {'value': obj.isoformat()}

    
    def deserialize(self, dict) -> Any:
        ...