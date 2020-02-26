import logging
from .process_agency_info import AgencyInfo
from .agency_api_service import AgencyApiService

from . import settings

settings.setup_logging()

logger = logging.getLogger(__name__)


# method invoked by lambda
def scrape_data(event, context=None):
    agencies = event["agencies"]
    if event.get("agencies", None) is None or len(agencies) <= 0:
        logger.warning("No Agency information was passed to scrape")
        return

    for agency in agencies:
        agency_instance = AgencyInfo(agency)
        agency_instance.process_agency_info()


if __name__ == "__main__":

    agency_api_service = AgencyApiService()
    agencies = agency_api_service.get_all_agencies()
    event = {"agencies": agencies}
    scrape_data(event)
    logger.info("Finished scraping")
