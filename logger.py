import logging

LOGGER = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
LOGGER.addHandler(stream_handler)

LOGGER.setLevel(logging.INFO)
