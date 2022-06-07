import logging
import sys

__all__ = ["LOGGER"]

DEFAULT_FORMATTER = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
DEFAULT_HANDLER = logging.StreamHandler(sys.stdout)
DEFAULT_HANDLER.setFormatter(DEFAULT_FORMATTER)

LOGGER = logging.getLogger(".".join(__name__.split(".")[:-1]))
LOGGER.setLevel(logging.INFO)
LOGGER.addHandler(DEFAULT_HANDLER)
