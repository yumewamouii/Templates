from src.models.base_model import BaseModel
from src.exceptions.validation import ArgumentException


class ModelMetadata:
    @staticmethod
    def get_models() -> list:
        result = []
        for inheritor in BaseModel.__subclasses__():
            result.append(inheritor.__name__)
    

    @staticmethod
    def get_fields(model: BaseModel, flat_fields_only: bool = True) -> list[str]:
        if model is None:
            raise ArgumentException(f'An instance of this model cannot be None')
        

        # Если это dataclass — брать поля напрямую
        if hasattr(model, '__dataclass_fields__'):
            return list(model.__dataclass_fields__.keys())

        # Если передан экземпляр dataclass
        if hasattr(model.__class__, '__dataclass_fields__'):
            return list(model.__class__.__dataclass_fields__.keys())
        

        result = []
        for name in dir(model):
            if name.startswith('_') or name.startswith('__'):
                continue


            value = getattr(model, name)
            if flat_fields_only and isinstance(value, (dict, list)):
                continue


            result.append(name)
        

        return result