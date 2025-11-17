from typing import TypeVar, Generic

# Define generic type variables for the left and right values
L = TypeVar('L')
R = TypeVar('R')


class Either(Generic[L, R]):
    """
    A functional-style Either container that can hold one of two possible values:
    - Left (usually represents an error or alternative result)
    - Right (usually represents a successful result)

    Only one of the two sides should be set at a time.
    """

    @classmethod
    def with_left(cls, value):
        """
        Factory method to create an Either instance with a left value.
        Typically used to represent an error or a failure case.
        """
        return cls(value, None)

    @classmethod
    def with_right(cls, value):
        """
        Factory method to create an Either instance with a right value.
        Typically used to represent a successful result.
        """
        return cls(None, value)

    def __init__(self, left: L, right: R):
        """
        Initialize an Either with left and right values.
        One of them should be None.
        """
        self._left = left
        self._right = right

    @property
    def is_left(self) -> bool:
        """Returns True if this Either holds a left value."""
        return self._left is not None

    @property
    def is_right(self) -> bool:
        """Returns True if this Either holds a right value."""
        return self._right is not None

    @property
    def left(self) -> L:
        """Returns the left value (may be None if this is a right)."""
        return self._left

    @property
    def right(self) -> R:
        """Returns the right value (may be None if this is a left)."""
        return self._right
