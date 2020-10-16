import logging
import colorlog


# Global Vars
color = {
    "green": "#61ff33",
    "yellow": "#ecff33",
    "red": "#D00000"
}
#############


def create_log_file(log_file_name):
    with open(log_file_name, 'w') as o: pass


def setup_logger(log_fmt="%(log_color)s%(asctime)s:%(levelname)s:%(message)s", log_file_name=".output.log", level='DEBUG'):

    # a new log file is created each time.
    # no space issues are caused.
    create_log_file(log_file_name)

    formatter = colorlog.ColoredFormatter(
        log_fmt,
        datefmt='%D'
    )

    logger = logging.getLogger()

    handler2 = logging.FileHandler(log_file_name)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.addHandler(handler2)
    logger.setLevel(level)

    return logger