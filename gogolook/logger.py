import logging
from typing import Dict

import orjson
import structlog

from gogolook.config import Settings

LOG_LEVELS: Dict[str, int] = {
    "critical": logging.CRITICAL,
    "error": logging.ERROR,
    "warning": logging.WARNING,
    "info": logging.INFO,
    "debug": logging.DEBUG,
}


def get_logger(settings: Settings):
    structlog.configure(
        cache_logger_on_first_use=True,
        wrapper_class=structlog.make_filtering_bound_logger(
            LOG_LEVELS[settings.LOG_LEVEL]
        ),
        processors=[
            structlog.threadlocal.merge_threadlocal_context,
            structlog.processors.add_log_level,
            structlog.processors.format_exc_info,
            structlog.processors.TimeStamper(fmt="iso", utc=True),
            structlog.processors.JSONRenderer(serializer=orjson.dumps),
        ],
        logger_factory=structlog.BytesLoggerFactory(),
    )

    logger = structlog.get_logger()
    return logger
