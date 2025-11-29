from typing import Generic, TypeVar


import reactivex as rx


T = TypeVar('T')


class BaseManager(Generic[T]):
    def __init__(self, default_state: T):
        self._stream = rx.subject.BehaviorSubject(default_state)
    


    @property
    def stream(self) -> rx.Observable[T]:
        return self._stream
    

    @property
    def state(self) -> T:
        return self._stream.value
    

    @state.setter
    def state(self, value: T):
        self._stream.on_next(value)
    

    def emit_error(self, error: Exception):
        self._stream.on_next(self.state.with_error(error))