"""
Functions for debugging.
"""
import logging
from datetime import datetime
from functools import wraps
from pathlib import Path

from paths import LOG_DIR

LOGGER = logging.getLogger(__name__)

# Set this flag to turn on debugging.
DEBUG = True

# Format for datetime in log file name.
LOG_DATE_FMT = "%Y%m%d_%H%M%S"


def create_filelog(thrd_name):
    """Create a file to be the debug log for this run."""
    if DEBUG:
        LOG_DIR.mkdir(exist_ok=True)
        log_file = LOG_DIR / f"dbg_{thrd_name}_{datetime.now().strftime(LOG_DATE_FMT)}.log"
        return logging.FileHandler(log_file, mode="w")
    else:
        return logging.NullHandler()
