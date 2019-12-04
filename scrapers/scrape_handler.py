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
    os.environ['GOOGLE_API_KEY'] = ""
    agency_api_service = AgencyApiService()
    agencies = agency_api_service.get_all_agencies()
    event = {
        "agencies": [
            {
                "id": 2,
                "name": "Traffic, Parking & Transportation",
                "website": "https://www.cambridgema.gov/traffic",
                "twitter": "",
                "facebook": "",
                "phone_number": "617-349-4242",
                "address": "795 Massachusetts Ave.   Cambridge,\\r \\t\\t\\t\\t\\t\\tMA 02139",
                "description": "",
                "last_successful_scrape": "2019-07-07T00:23:58.830316Z",
                "scrape_counter": 10
            }
        ]
    }
    scrape_data(event)
    print("SCRAPED")
