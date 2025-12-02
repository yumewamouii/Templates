from typing import Generic, TypeVar


from src.exceptions.validation import ArgumentException


T = TypeVar('T')


class Observer(Generic[T]):
    def update(self, state: T) -> None:
        """
        Update the state of the observer.

        Args:
            state (T): The new state to be updated.
        """
        if not isinstance(state, T):
            raise ArgumentException(
                f"Expected state of type {T.__name__}, but got {type(state).__name__}"
            )
        pass