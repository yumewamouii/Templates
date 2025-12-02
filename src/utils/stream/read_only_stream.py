from typing import TypeVar, Callable


from utils.observer.base_observable import BaseObservable, StreamSubscription


T = TypeVar('T')


class ReadOnlyStream(BaseObservable[T]):
    """
    A stream that only provides a subscription,
    but it does not allow you to assign values.
    """
    def __init__(self, stream: BaseObservable[T]):
        self._stream = stream

    
    def subscribe(self, call: Callable[[T], None]) -> StreamSubscription[T]:
        return self._stream.subscribe(call)
    

    def unsubscribe(self, subscription: StreamSubscription) -> None:
        return self._stream.unsubscribe(subscription)