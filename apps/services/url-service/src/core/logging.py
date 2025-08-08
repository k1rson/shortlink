import sys
from loguru import logger

logger.remove()

custom_format = (
    "<green>{time:YY-MM-DD HH:mm:ss}</green> | "
    "<cyan>{module:12}</cyan> | "
    "<level>{level:8}</level> | "
    "<yellow>{name:25}</yellow> | "
    "<level>{message}</level>"
)

logger.add(
    sys.stdout,
    format=custom_format,
    level="DEBUG",
    enqueue=True,
    colorize=True,
    diagnose=False,
)

__all__ = ["logger"]
