import logging


class Logger:

    __logger = None

    __logging = None

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
    def start_logger(log_file_path):
        logging.basicConfig(filename=log_file_path, format='%(asctime)s %(message)s')
        Logger.__logging = logging.getLogger('main')
        Logger.__logging.setLevel(logging.DEBUG)

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
        Logger.__logging.warning('Warning: ' + message)

    """ Adds a error log to the log file with the given message"""

    @staticmethod
    def error_log(message: str):
        if Logger.__logging is None:
            raise Exception('Logger not initiated')
        Logger.__logging.error('Error: ' + message)

    """ Adds a critical event log to the log file with the given message"""

    @staticmethod
    def critical_log(message: str):
        if Logger.__logging is None:
            raise Exception('Logger not initiated')
        Logger.__logging.critical('Critical: ' + message)

