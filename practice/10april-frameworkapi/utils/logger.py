import logging
import os

def get_logger(name):

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:

        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        file_handler = logging.FileHandler(f"{log_dir}/test.log")
        console_handler = logging.StreamHandler()


        formatter = logging.Formatter("%(asctime)s", datefmt="%Y-%m-%d %H:%M:%S")

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger