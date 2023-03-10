from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from . import my_constants
import logging
print("Hello!")


def add_log(message, level=logging.INFO, real_time=False, log_file=f"{my_constants.logs_dir}\logs.log"):
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.log(level, message)
