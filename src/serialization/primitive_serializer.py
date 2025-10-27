from typing import Any


from src.serialization.base_serializer import BaseSerializer


from src.exceptions.validation import ArgumentException


class PrimitiveSerializer(BaseSerializer):
    def serialize(self, obj: Any) -> dict[str, Any]:
        if not isinstance(obj, (int, float, str, bool)):
            raise ArgumentException(f'Excepted int, float, str or bool. Got {type(obj).__name__}')
        

        return {'value': obj}


    def deserialize(self, data, cls):
        ...