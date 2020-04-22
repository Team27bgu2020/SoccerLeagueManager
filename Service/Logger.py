import logging

log_file = ''


class Logger:

    def __init__(self):
        logging.basicConfig(filename=log_file, format='%(asctime)s %(message)s')
        self.__logger = logging.getLogger('main')

    def info_log(self, message: str):
        self.__logger.info(message)

    def warning_log(self, message: str):
        self.__logger.warning(message)

    def error_log(self, message: str):
        self.__logger.error(message)

    def critical_log(self, message: str):
        self.__logger.critical(message)