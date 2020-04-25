import logging

log_file = ''

logging.basicConfig(filename=log_file, format='%(asctime)s %(message)s')
logger = logging.getLogger('main')

""" Adds a information log to the log file with the given message"""


def info_log(message: str):
    logger.info(message)


""" Adds a warning log to the log file with the given message"""


def warning_log(message: str):
    logger.warning(message)


""" Adds a error log to the log file with the given message"""


def error_log(message: str):
    logger.error(message)


""" Adds a critical event log to the log file with the given message"""


def critical_log(message: str):
    logger.critical(message)


def define_log_path(path):

    if Logger.log_file == '':
        Logger.log_file = path