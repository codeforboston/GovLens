import os
import logging
from process_agency_info import AgencyInfo
from agency_api_service import AgencyApiService

# method invoked by lambda
def scrape_data(event, context=None):
    agencies = event["agencies"]
    if event.get("agencies", None) is None or len(agencies) <= 0:
        print("No Agency information was passed to scrape")
        return

    for agency in agencies:
        agency_instance = AgencyInfo(agency)
        agency_instance.process_agency_info()


# if running from local, we get the list of agencies and scrape one by one.
if __name__ == "__main__":
    # If running from local, set the environment variable to your local
    logging.basicConfig(filename='Scraper_Errors.log', level=logging.ERROR, format='%(asctime)s %(message)s')
    os.environ['govlens_api'] = "http://govlens.us-east-2.elasticbeanstalk.com/api/agencies/"
    agency_api_service = AgencyApiService()
    agencies = agency_api_service.get_all_agencies()
    event = {
        "agencies": agencies
    }
    scrape_data(event)
    print("SCRAPED")
