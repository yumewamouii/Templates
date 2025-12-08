from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Callable, Optional, List


from src.utils.stream.stream_subscription import StreamSubscription


from src.utils.observer.observer import Observer

T = TypeVar('T')


class BaseObservable(ABC, Generic[T]):
    @abstractmethod
    def subscribe(self, call: Callable[[T], None]) -> StreamSubscription[T]:
        """
        Subscribes to the stream.

        Args:
            call: The function called during the update.

        Returns:
            StreamSubscription: An object for unsubscribing.
        """
        pass


    @abstractmethod
    def unsubscribe(self, subscription: StreamSubscription) -> None:
        """
        Unsubscribes the observer.

        Args:
            subscription: Subscription for deletion.
        """
        pass


class ObservableSubject(BaseObservable[T]):
    def __init__(self):
        self._observers: List[Observer[T]] = []
        self._subscriptions: List[StreamSubscription[T]] = []
    

    def subscribe(self, call: Callable[[T], None]) -> StreamSubscription[T]:
        subscription = StreamSubscription(self, call)
        observer = _SubscriptionObserver(subscription)

        self._subscriptions.append(subscription)
        self._observers.append(observer)

        return subscription

    def unsubscribe(self, subscription: StreamSubscription[T]) -> None:
        if subscription in self._subscriptions:
            idx = self._subscriptions.index(subscription)

            self._subscriptions.pop(idx)
            self._observers.pop(idx)
    

    def notify_observers(self, data: T) -> None:
        """
        Notifies all observers about the update.
        """
        for observer in self._observers:
            observer.update(data)


class _SubscriptionObserver(Observer[T]):
    """
    A wrapper that turns a Callable into an Observer.
    """


    def __init__(self, subscription: StreamSubscription[T]):
        self._subscription = subscription

    def update(self, data: T) -> None:
        self._subscription.notify(data)