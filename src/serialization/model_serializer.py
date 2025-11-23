from typing import Any


from src.serialization.base_serializer import BaseSerializer


from src.models.base_model import BaseModel


from src.reports.base_report import BaseReport


from src.exceptions.validation import ArgumentException


from src.utils.fields import ValidatedField


class ModelSerializer(BaseSerializer):
    def serialize(self, obj: BaseModel) -> dict[str, Any]:
        if not isinstance(obj, BaseModel):
            raise ArgumentException(f'Excepted model. Got {type(obj).__name__}')
        
    
        return self.serialize_model(model=obj)
    

    def serialize_model(self, model: Any) -> dict:
        def extract_properties(obj: Any) -> dict:
            return {
                name: getattr(obj, name)
                for name, attr in obj.__class__.__dict__.items()
                if isinstance(attr, ValidatedField)
            }

        serialized = extract_properties(model)

        if isinstance(model, BaseModel):
            serialized['id'] = model.id

        for key, value in serialized.items():
            if isinstance(value, list):
                serialized[key] = [self.serialize_model(item) for item in value]
            elif hasattr(value, '__dict__'):
                serialized[key] = self.serialize_model(value)

        return serialized


    def deserialize(self, data, cls):
        ...