import requests, os 

class AgencyApiService:
    def __init__(self):
        # If environment variable is set, we use the corresponding api(usually local). otherwise govlens api
        if os.environ.get('govlens_api', None)  is None:
            self.base_url = "http://govlens.us-east-2.elasticbeanstalk.com/api/agencies/"
        else:
            self.base_url = os.environ['govlens_api']

    def get_all_agencies(self):
        try:
            all_agency_list = self._get(self.base_url)
            return all_agency_list
        except Exception as ex:
            print(f"Error while retrieving all the agency information: {str(ex)}")

    def _get(self, url):
        response = requests.get(url,headers={'Content-type': 'application/json'})
        return response.json()


