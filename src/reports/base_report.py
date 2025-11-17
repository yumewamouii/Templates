from abc import ABC, abstractmethod
from typing import Any


from src.models.base_model import BaseModel


from src.reports.report_format import ReportFormat


from src.utils.fields import ValidatedField


from src.serialization.model_serializer import ModelSerializer


class BaseReport(ABC):
    def create(self, obj: list[BaseModel]) -> str:
        serializer = ModelSerializer()
        serialized_data = [serializer.serialize_model(item) for item in obj]
        return self.create_from_serialized(serialized_data, obj)

    @abstractmethod
    def create_from_serialized(self, serialized: list[dict], original: list[BaseModel]) -> str:
        # method for generation report from serialized data
        pass
    

    def _flatten_dict(self, data: dict, parent_key: str = '', sep: str = '.') -> dict:
        # Converts a nested dictionary to a flat delimited format.
        flattened = {}


        for key, value in data.items():
            full_key = f'{parent_key}{sep}{key}' if parent_key else key

            if isinstance(value, dict):
                nested = self._flatten_dict(value, full_key, sep)
                flattened.update(nested)
            else:
                flattened[full_key] = value
        

        return flattened