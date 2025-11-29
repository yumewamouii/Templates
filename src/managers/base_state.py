from copy import deepcopy


class BaseState:
    def __init__(self, error = None):
        self._error = error
    

    @property
    def error(self):
        return self._error
    

    def with_error(self, value: Exception):
        state = deepcopy(self)
        state._error = value
        return state