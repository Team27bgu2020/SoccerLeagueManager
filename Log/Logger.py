import logging
import os.path

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')


class Logger:
    __logger = None
    __logging = None
    __error_logging = None

    @staticmethod
    def get_instance():

        if Logger.__logger is None:
            Logger()
        return Logger.__logger

    def __init__(self):

        if Logger.__logger is not None:
            raise Exception("Unauthorized access to Logger constructor")
        else:
            Logger.__logger = self

    @staticmethod
    def start_logger(log_file_path=os.path.dirname(__file__) + "\\LogFiles\\Event_Log.txt",
                     error_file_path=os.path.dirname(__file__) + "\\LogFiles\\Error_Log.txt"):
        # logging.basicConfig(filename=log_file_path, format=formatter)
        handler = logging.FileHandler(log_file_path)
        handler.setFormatter(formatter)
        Logger.__logging = logging.getLogger('main')
        Logger.__logging.setLevel(logging.DEBUG)
        Logger.__logging.addHandler(handler)

        handler = logging.FileHandler(error_file_path)
        handler.setFormatter(formatter)
        Logger.__error_logging = logging.getLogger('error_log')
        Logger.__error_logging.setLevel(logging.DEBUG)
        Logger.__error_logging.addHandler(handler)

    """ Adds a information log to the log file with the given message"""

    @staticmethod
    def info_log(message: str):
        if Logger.__logging is None:
            raise Exception('Logger not initiated')
        Logger.__logging.info('Info: ' + message)

    """ Adds a warning log to the log file with the given message"""

    @staticmethod
    def warning_log(message: str):
        if Logger.__logging is None:
            raise Exception('Logger not initiated')
        Logger.__error_logging.warning('Warning: ' + message)

    """ Adds a error log to the log file with the given message"""

    @staticmethod
    def error_log(message: str):
        if Logger.__logging is None:
            raise Exception('Logger not initiated')
        Logger.__error_logging.error('Error: ' + message)

    """ Adds a critical event log to the log file with the given message"""

    @staticmethod
    def critical_log(message: str):
        if Logger.__logging is None:
            raise Exception('Logger not initiated')
        Logger.__error_logging.critical('Critical: ' + message)
