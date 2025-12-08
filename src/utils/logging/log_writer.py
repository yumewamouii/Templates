import datetime


from src.settings_manager import SettingManager


from src.utils.logging.log import Log
from src.utils.logging.logger import Logger


class LogWriter:
    """
    Handles persistent log output by subscribing to emitted log events and writing
    them to a file when they meet the configured log-level threshold.
    """
    _setting_manager: SettingManager


    def __init__(self, setting_manager: SettingManager):
        """
        Initialize the LogWriter with a settings manager that controls logging behavior.

        Parameters:
            setting_manager (SettingManager): Provides configuration, including log level.
        """
        self._setting_manager = setting_manager
    

    def setup(self):
        """
        Subscribe to the global logger's event stream, enabling automatic log capture.
        """
        Logger.watch_logs().subscribe(self.write)
    

    def write(self, log: Log):
        """
        Process and persist a log entry if it meets the configured log-level threshold.

        Parameters:
            log (Log): The log entry to handle.
        """
        if self._setting_manager.settings.log_level.value >= log.level.value:
            log_str = f'{log.level} [{datetime.datetime.now().isoformat()}] {log.tag}: {log.message}'
            with open('logs.txt', 'a') as log_file:
                log_file.write(log_str + '\n')
                log_file.flush()
            print(log_str)