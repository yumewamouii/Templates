from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Callable


T = TypeVar('T')


class BaseObservable(ABC, Generic[T]):
    @abstractmethod
    def subscribe(self, call: Callable[[T], None]):
        pass


    @abstractmethod
    def unsubscribe(self, subscription: 'StreamSubscription'):
        pass


class StreamSubscription(Generic[T]):
    def __init__(self, stream: BaseObservable[T], call: Callable[[T], None]):
        self._stream = stream
        self._call = call
    

    def call(self, data: T):
        self._call(data)
    

    def close(self):
        self._stream.unsubscribe(self)
        self._stream = None