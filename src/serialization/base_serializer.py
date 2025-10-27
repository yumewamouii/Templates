from abc import abstractmethod, ABC
from typing import Any


class BaseSerializer(ABC):
    @abstractmethod
    def serialize(self, obj: Any) -> dict[str, Any]:
        pass


    @abstractmethod
    def deserialize(self, data: dict, cls: type) -> Any:
        pass