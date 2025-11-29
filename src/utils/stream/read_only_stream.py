from typing import TypeVar, Callable


from src.utils.stream.base_observable import BaseObservable, StreamSubscription


T = TypeVar('T')


class ReadOnlyStream(BaseObservable[T]):
    def __init__(self, stream: BaseObservable[T]):
        self._stream = stream

    
    def subscribe(self, call: Callable[[T], None]) -> StreamSubscription:
        return self._stream.subscribe(call)
    

    def unsubscribe(self, subscription: StreamSubscription):
        return self._stream.unsubscribe(subscription)