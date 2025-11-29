from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, List


from src.utils.stream.base_observable import BaseObservable
from src.utils.stream.streams import EventStream


from src.models.base_model import BaseModel
from src.models.filter import Filter


K = TypeVar('K')
V = TypeVar('V', bound = BaseModel)


class BaseStorage(Generic[K, V], ABC):
    _deletions: EventStream[str]
    _updates: EventStream[V]


    def __init__(self):
        self._deletions = EventStream()
        self._updates = EventStream()
    

    @property
    def deletions(self) -> BaseObservable[str]:
        return self._deletions.as_read_only()
    

    @property
    def updates(self) -> BaseObservable[V]:
        return self._updates.as_read_only()


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


    
    def update(self, key: K, value: V):
        self._update_internal(key, value)
        self._updates.emit(value)


    @abstractmethod
    def _update_internal(self, key: K, value: V):
        pass


    def delete(self, key: K):
        self._delete_internal(key)
        self._deletions.emit(key)
    

    @abstractmethod
    def _delete_internal(self, key: K):
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