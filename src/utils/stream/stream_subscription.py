from typing import Generic, Optional, Callable, TypeVar


from src.utils.observer.base_observable import BaseObservable


T = TypeVar('T')


class StreamSubscription(Generic[T]):
    def __init__(self, stream: "BaseObservable[T]", callback: Callable[[T], None]) -> None:
        self._stream: Optional["BaseObservable[T]"] = stream
        self._callback: Optional[Callable[[T], None]] = callback
    

    def notify(self, data: T) -> None:
        """
        Observable is called to transfer data.
        """
        if self._callback is not None:
            self._callback(data)
    

    # For compatibility: subscription can be called as a function.
    __call__ = notify
    

    def close(self) -> None:
        """
        Unsubscribes itself from Observable.
        """
        if self._stream is not None:
            self._stream.unsubscribe(self)

        self._stream = None
        self._callback = None