from abc import ABC, abstractmethod
from typing import TypeVar, Generic

# Define a generic type variable for the model type
MODEL = TypeVar('MODEL')


class BaseTypeMapper(ABC, Generic[MODEL]):
    """
    Abstract base class for type mappers.
    Provides a template for converting between data representations and model objects.
    """

    @abstractmethod
    def from_model(self, obj):
        """
        Convert a model object into another data representation.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def to_model(self, data) -> MODEL:
        """
        Convert data (e.g., a dictionary or DTO) into a model object.
        Must be implemented by subclasses.
        """
        pass
