from abc import ABC, abstractmethod
#from src.core.validator


class AbstractBaseModel(ABC):
    __id: str


    @abstractmethod
    def __init__(self):
        pass
    

    @property
    @abstractmethod
    def id(self) -> str:
        pass


    @id.setter
    @abstractmethod
    def id(self, value: str) -> str:
        pass


    @abstractmethod
    def __eq__(self, value: str) -> bool:
        return self.__id == value

