from typing import Any


from src.serialization.base_serializer import BaseSerializer


from src.models.base_model import BaseModel


from src.reports.base_report import BaseReport


from src.exceptions.validation import ArgumentException


class ModelSerializer(BaseSerializer):
    def serialize(self, obj: BaseModel) -> dict[str, Any]:
        if not isinstance(obj, BaseModel):
            raise ArgumentException(f'Excepted model. Got {type(obj).__name__}')
        
    
        return BaseReport._serialize_model(model=obj)


    def deserialize(self, data, cls):
        ...