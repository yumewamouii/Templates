from enum import Enum


from src.utils.enum_meta import EnumMeta


class LogLevel(Enum, metaclass = EnumMeta):
    """Represents the available logging levels used throughout the application."""
    DEBUG = 0
    INFO = 1
    ERROR = 2


class Log:
    """
    Encapsulates a single log entry consisting of a log level, a tag identifying
    the log source, and a message describing the logged event.
    """
    _level: LogLevel = None
    _tag: str = None
    _message: str = None


    def __init__(self, level: LogLevel, tag: str, message: str):
        """
        Initialize a new log entry.

        Parameters:
            level (LogLevel): The severity level of the log.
            tag (str): A short identifier indicating the log source.
            message (str): The log message content.
        """
        self._level = level
        self._tag = tag
        self._message = message
    

    @property
    def level(self) -> LogLevel:
        """Return the severity level of the log entry."""
        return self._level
    

    @property
    def tag(self) -> str:
        """Return the tag identifying the log source."""
        return self._tag
    

    @property
    def message(self) -> str:
        """Return the log message content."""
        return self._message