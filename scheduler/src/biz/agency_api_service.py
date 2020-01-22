import requests


class AgencyApiService:
    def __init__(self):
        self.base_url = "http://govlens.us-east-2.elasticbeanstalk.com/api/agencies/"

    def get_all_agencies(self):
        try:
            agency_list = self._get(self.base_url)
            return agency_list
        except Exception as ex:
            print(f"Error while retrieving all the agency information: {str(ex)}")
            return []

    def _get(self):
        try:
            response = requests.get(
                self.base_url, headers={"Content-type": "application/json"}
            )
            response_json = response.json()
            print(f"received {len(response_json)} agencies from {self.base_url}")
            return response_json
        except Exception as ex:
            print(f"Error while retrieving agency list from {self.base_url}: {str(ex)}")
            return []
