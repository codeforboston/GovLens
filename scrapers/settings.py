"""Unified configuration for GovLens scraper

Goals of this file:
    - Express the entire configuration of the scraper in one place
    - Quickly fail in the event of an improper configuration
"""
import logging
import os
import sys


logger = logging.getLogger(__name__)


def setup_logging():
    """configure logging

    call this as soon as possible
    """
    try:
        import coloredlogs

        coloredlogs.install(level=logging.INFO)
    except Exception:
        logger.warning("Could not import coloredlogs")
        # fall back to basicConfig
        logging.basicConfig(level=logging.INFO,)


# setup the logger
setup_logging()

# attempt to load variables from a file called '.env'
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    logger.warning(
        "dotenv could not be imported. Variables will only be loaded from the environment."
    )

GOVLENS_API_TOKEN = os.environ.get("GOVLENS_API_TOKEN")
GOVLENS_API_ENDPOINT = os.environ.get("GOVLENS_API_ENDPOINT")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

if not GOVLENS_API_ENDPOINT:
    logger.warning(
        "The environmental variable GOVLENS_API_ENDPOINT was not provided. Exiting..."
    )
    sys.exit(1)

if not GOVLENS_API_TOKEN:
    logger.warning(
        "The environmental variable GOVLENS_API_TOKEN was not provided. Exiting..."
    )
    sys.exit(1)

if not GOOGLE_API_KEY:
    logger.warning(
        "The environmental variable GOOGLE_API_KEY was not provided; no lighthouse data will be collected."
    )
