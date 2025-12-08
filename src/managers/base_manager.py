from typing import Generic, TypeVar, List, Callable


from src.exceptions.validation import OperationException


from src.utils.observer.observer import Observer
from src.utils.observer.base_observable import ObservableSubject, BaseObservable


from src.managers.base_state import BaseState

T = TypeVar('T', bound = 'BaseState')



class BaseManager(Generic[T]):
    def __init__(self, default_state: T):
        """
        Initializes the manager with the initial state.

        Args:
            default_state (T): Initial state.
        """


        self._state = default_state
        self._subject = ObservableSubject[T]()
    

    @property
    def stream(self) -> BaseObservable[T]:
        """
        Returns an observable stream that allows subscribing to state changes.

        Returns:
            BaseObservable[T]: The subscription stream.
        """


        return self._subject
    

    @property
    def state(self) -> T:
        """
        Returns the current state.

        Returns:
            T: Current status.
        """


        return self._state
    

    @state.setter
    def state(self, value: T):
        """
        Sets a new state and notifies all subscribers.

        Args:
            value (T): New state.
        """


        self._state = value
        self._subject.notify_observers(value)
    

    def emit_error(self, error: OperationException):
        """
        Generates a new error state using the with_error method of the current state.

        It is assumed that the state type T supports the with_error(error) method.

        Args:
            error (Exception): An error for switching to a new state.
        """


        new_state = self._state.with_error(error) #type: ignore
        self.state = new_state
