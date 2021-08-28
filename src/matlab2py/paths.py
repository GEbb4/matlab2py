"""
Paths within this package.
"""
import logging
from pathlib import Path

LOGGER = logging.getLogger(__name__)

# The root directory of the module.
MODULE_DIR = Path(__file__).parent.resolve()

# The overall project root directory (i.e. the top-level of a checkout).
PROJECT_DIR = MODULE_DIR.parent.parent

# Directory which is ignored by .gitignore for all logging.
LOG_DIR = PROJECT_DIR / "logs"
