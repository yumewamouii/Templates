from typing import Generic, TypeVar, Callable, List
from abc import abstractmethod, ABC


from src.utils.stream.stream_subscription import StreamSubscription
from src.utils.stream.read_only_stream import ReadOnlyStream


from src.utils.observer.base_observable import BaseObservable
from src.utils.observer.observer import Observer 


T = TypeVar('T')


class BaseStream(BaseObservable[T], ABC):
    """
    The stream that:
    - stores pairs (subscription, observer)
    - notifies observer objects in emit()
    """
    

    def __init__(self):
        self._subscriptions: List[StreamSubscription[T]] = []
        self._observers: List[Observer[T]] = []
    

    def as_read_only(self) -> ReadOnlyStream[T]:
        return ReadOnlyStream(self)
    

    def subscribe(self, call: Callable[[T], None]) -> StreamSubscription[T]:
        subscription = StreamSubscription(self, call)
        observer = _SubscriptionObserver(subscription)

        self._subscriptions.append(subscription)
        self._observers.append(observer)

        self._subscribe_internal(subscription)

        return subscription
    

    def unsubscribe(self, subscription: StreamSubscription[T]) -> None:
        if subscription in self._subscriptions:
            idx = self._subscriptions.index(subscription)
            self._subscriptions.pop(idx)
            self._observers.pop(idx)
    

    @abstractmethod
    def emit(self, value: T) -> None:
        """
        Child classes simply call notify_observers.
        """
        pass


    def notify_observers(self, value: T) -> None:
        for observer in list(self._observers):
            observer.update(value)

    def _subscribe_internal(self, subscription: StreamSubscription[T]) -> None:
        pass


class _SubscriptionObserver(Observer[T]):
    """
    The observer that is proxying the subscription.notify() call.
    """

    def __init__(self, subscription: StreamSubscription[T]):
        self._subscription = subscription

    def update(self, data: T) -> None:
        self._subscription.notify(data)