from typing import Any
from datetime import datetime
import json


from src.serialization.base_serializer import BaseSerializer
from src.serialization.primitive_serializer import PrimitiveSerializer
from src.serialization.datetime_serializer import DatetimeSerializer
from src.serialization.model_serializer import ModelSerializer


from src.models.base_model import BaseModel


from src.exceptions.validation import OperationException, ArgumentException


class SerializerFactory:
    def __init__(self):
        self._serializer_map = {
            'primitive': PrimitiveSerializer,
            'datetime': DatetimeSerializer,
            'model': ModelSerializer
        }
    

    def get_serializer(self, obj: Any) -> BaseSerializer:
        for serializer_cls in self._serializer_map.values():
            serializer = serializer_cls()
            try:
                data = serializer.serialize(obj)
                return json.dumps(data)
            except ArgumentException:
                continue
        raise ArgumentException(f'No suitable serializer found for type: {type(obj).__name__}')