import logging
from Flaskblog.config.config import LOG_FILE, LOG_FORMAT, LOG_LEVEL, LOG_NAME
from functools import wraps


def create_logger():
    """
    Creates a logging object
    """
    logger = logging.getLogger(LOG_NAME)
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(LOG_LEVEL)
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT.replace('?', '%')))
    logger.addHandler(file_handler)
    return logger


def log_error(function):
    """
    Writes errors in log file
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            logger = create_logger()
            exc = "There was an exception in  " + function.__name__
            logger.exception(exc)
    return wrapper
