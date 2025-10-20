from dataclasses import asdict, dataclass


from src.utils.validator import Validator
from src.utils.model_metadata import ModelMetadata


from src.exceptions.validation import OperationException


@dataclass
class BaseDTO:
    def to_dict(self):
        return asdict(self)
    

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
    

    @classmethod
    def create(cls, data: dict) -> 'BaseDTO':
        Validator.validate(data, dict)
        fields = ModelMetadata.get_fields(cls)
        matching_keys = [key for key in data.keys() if key in fields]


        try:
            init_data = {key: data[key] for key in matching_keys}
            return cls(**init_data)
        except:
            raise OperationException('Unable to upload data')