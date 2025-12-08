from abc import ABC, abstractmethod


from src.store.base_storage import BaseStorage, K, V
from src.store.list_filterer import ListFilterer


from src.models.filter import Filter


from src.utils.logging.logger import Logger


class BaseMemoryStorage(BaseStorage[K, V], ABC):
    def __init__(self):
        super().__init__()
        self._data = {}


    @property
    def _key(self):
        return self.__class__.__name__
    
    
    def contains_key(self, key: K) -> bool:
        return key in self._data
    

    def get(self, key: K) -> V | None:
        return self._data.get(key)
    

    def get_all(self, offset: int = 0, limit: int | None = None) -> list[V]:
        values = list(self._data.values())
        if limit is not None:
            values = values[offset:offset + limit]
        else:
            values = values[offset:]
        return values
    

    def create(self, value: V):
        self._data[value.id] = value
        Logger.info(self._key, f'Created {value.id}')
    

    def _update_internal(self, key: K, value: V):
        self._data[key] = value
        Logger.info(self._key, f'Updated {value.id}')
    

    def _delete_internal(self, key: K):
        if key in self._data:
            del self._data[key]
            Logger.info(self._key, f'Deleted {key}')
        else:
            Logger.info(self._key, f'Could not delete {key} because it does not exist')
    

    def clear(self):
        self._data.clear()
        Logger.info(self._key, 'Cleared')
    
    
    def is_empty(self) -> bool:
        return len(self._data) == 0


    def get_filtered(self, filters: list[Filter]) -> list[V]:
        return ListFilterer.apply_filters(self._data.values(), filters)