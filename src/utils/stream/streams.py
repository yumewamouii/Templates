from typing import TypeVar


from src.utils.stream.base_observable import StreamSubscription
from src.utils.stream.base_stream import BaseStream


T = TypeVar('T')


class EventStream(BaseStream[T]):
    # Hot channel

    def emit(self, value: T):
        for subscription in self._subscriptions:
            subscription.call(value)
    

class ValueStream(BaseStream[T]):
    # Cold flow

    _value: T | None = None


    @classmethod
    def seeded(cls, value: T):
        stream = cls()
        stream.emit(value)
        return stream
    

    def emit(self, value: T):
        for subscription in self._subscriptions:
            subscription.call(value)
    

    def _subscribe_internal(self, subscription: StreamSubscription):
        subscription.call(self._value)