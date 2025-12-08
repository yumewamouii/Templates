from src.utils.logging.log import Log, LogLevel


from src.utils.stream.base_stream import BaseObservable


from src.utils.stream.streams import EventStream


class Logger:
    """
    Provides a centralized logging mechanism that emits log events to an observable
    stream. Consumers can subscribe to this stream to receive log entries in real time.
    """
    _log_events: EventStream[Log] = EventStream()
    

    @staticmethod
    def watch_logs() -> BaseObservable[Log]:
        """
        Return a read-only observable stream of log events.

        Returns:
            BaseObservable[Log]: A read-only observable that emits Log instances.
        """     
        return Logger._log_events.as_read_only()
    

    @staticmethod
    def log(level: LogLevel, tag: str, message: str):
        """
        Create and emit a log entry with a specified level, tag, and message.

        Parameters:
            level (LogLevel): The severity of the log entry.
            tag (str): Identifier of the log source.
            message (str): Description of the logged event.
        """
        log = Log(level, tag, message)
        Logger._log_events.emit(log)
    

    @staticmethod
    def debug(tag: str, message: str):
        """
        Emit a debug-level log entry.

        Parameters:
            tag (str): Identifier of the log source.
            message (str): Description of the logged event.
        """
        Logger.log(LogLevel.DEBUG, tag, message)
    

    @staticmethod
    def info(tag: str, message: str):
        """
        Emit an info-level log entry.

        Parameters:
            tag (str): Identifier of the log source.
            message (str): Description of the logged event.
        """
        Logger.log(LogLevel.INFO, tag, message)
    

    @staticmethod
    def error(tag: str, message: str):
        """
        Emit an error-level log entry.

        Parameters:
            tag (str): Identifier of the log source.
            message (str): Description of the logged event.
        """
        Logger.log(LogLevel.ERROR, tag, message)