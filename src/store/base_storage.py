from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, List


from src.models.base_model import BaseModel
from src.models.filter import Filter


K = TypeVar('K')
V = TypeVar('V', bound = BaseModel)


class BaseStorage(Generic[K, V], ABC):
    @abstractmethod
    def contains_key(self, key: K) -> bool:
        pass


    @abstractmethod
    def get(self, key: K) -> V | None:
        pass


    @abstractmethod
    def get_all(self, offset: int = 0, limit: int | None = None) -> list[V]:
        pass


    @abstractmethod
    def create(self, value: V):
        pass


    @abstractmethod
    def update(self, key: K, value: V):
        pass


    @abstractmethod
    def delete(self, key: K):
        pass


    @abstractmethod
    def clear(self):
        pass


    @abstractmethod
    def is_empty(self) -> bool:
        pass
    

    @abstractmethod
    def get_filtered(self, filters: list[Filter]) -> list[V]:
        pass