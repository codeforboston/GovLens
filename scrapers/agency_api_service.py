import requests
from scrape_data import scrape_data

class AgencyApiService:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000/api/agencies"

    def get_all_agencies(self):
        try:
            all_agency_list = self._get(self.base_url)
            return all_agency_list
        except Exception as ex:
            print(f"Error while retrieving all the agency information: {str(ex)}")

    def _get(self, url):
        response = requests.get(url,headers={'Content-type': 'application/json'})
        return response.json()

if __name__=="__main__":
    svc = AgencyApiService()
    agens = svc.get_all_agencies()
    scraped = scrape_data(agens)
    print ("SCRAPED")

