import logging


class ErrorLogger:
    __logger = None

    __logging = None

    @staticmethod
    def get_instance():

        if ErrorLogger.__logger is None:
            ErrorLogger()
        return ErrorLogger.__logger

    def __init__(self):

        if ErrorLogger.__logger is not None:
            raise Exception("Unauthorized access to Logger constructor")
        else:
            ErrorLogger.__logger = self

    def start_logger(log_file_path = "..\\..\\Log\\Error_Log.txt"):
        logging.basicConfig(filename=log_file_path, format="%(levelname)s %(asctime)s %(message)s")
        ErrorLogger.__logging = logging.getLogger('main')
        ErrorLogger.__logging.setLevel(logging.DEBUG)

    """ Adds a information log to the log file with the given message"""

    @staticmethod
    def info_log(message: str):
        if ErrorLogger.__logging is None:
            raise Exception('Logger not initiated')
        ErrorLogger.__logging.info('Info: ' + message)

    """ Adds a warning log to the log file with the given message"""

    @staticmethod
    def warning_log(message: str):
        if ErrorLogger.__logging is None:
            raise Exception('Logger not initiated')
        ErrorLogger.__logging.warning('Warning: ' + message)

    """ Adds a error log to the log file with the given message"""

    @staticmethod
    def error_log(message: str):
        if ErrorLogger.__logging is None:
            raise Exception('Logger not initiated')
        ErrorLogger.__logging.error('Error: ' + message)

    """ Adds a critical event log to the log file with the given message"""

    @staticmethod
    def critical_log(message: str):
        if ErrorLogger.__logging is None:
            raise Exception('Logger not initiated')
        ErrorLogger.__logging.critical('Critical: ' + message)


