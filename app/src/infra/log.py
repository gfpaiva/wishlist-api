import logging
import sys


def setup_logger():
    logger = logging.getLogger('src')
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(levelname)-9s [%(asctime)s] %(name)s: %(message)s')

    ch.setFormatter(formatter)

    logger.addHandler(ch)
