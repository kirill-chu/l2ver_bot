import logging
from logging.handlers import RotatingFileHandler

from constants import BASE_DIR, DATEFORMAT, LOG_COUNT, LOG_SIZE

LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'


def configure_logging():
    log_dir = BASE_DIR / 'logs'
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / 'l2ver_bot.log'
    rotating_handler = RotatingFileHandler(
        log_file, maxBytes=LOG_SIZE, backupCount=LOG_COUNT, encoding='utf-8')
    logging.basicConfig(
        datefmt=DATEFORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler()))
