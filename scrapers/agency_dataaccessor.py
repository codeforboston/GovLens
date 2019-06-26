import requests
from requests.auth import HTTPBasicAuth
import json, datetime


class AgencyDataAccessor:

    def __init__(self, token, agency_info):
        self.base_url = "http://127.0.0.1:8000/api/agencies/"
        self.agency_info = agency_info
        if token is None:
            self.token = "Token 0da08ca28219e9d154812a1e5b79d0405acbceeb"

    def update_scrape_info(self, scrape_info):
        try:
            outreach_and_communication = scrape_info['profile']['outreach_and_communication']
            self.agency_info['scrape_counter'] = self.agency_info['scrape_counter'] + 1

            contact_info = outreach_and_communication['contact_access']['info']
            self.agency_info['address'] = contact_info.get('address', None)
            self.agency_info['phone_number'] = contact_info.get('phone_number', None)
            
            # todo: get the twitter and facebook links
            social_media_info =  outreach_and_communication['social_media_access']['info']
            if len(social_media_info) > 0:
                self.agency_info['facebook'] = self.get_social_media_links(social_media_info, 'facebook')
                self.agency_info['twitter'] = self.get_social_media_links(social_media_info, 'twitter')
            else:
                print(f"social media informatioon not available for the agency {scrape_info['Website']}")

            self.agency_info['last_successful_scrape'] = datetime.datetime.now()
            agency_url = f"{self.base_url}{self.agency_info['id']}/"
            response = requests.put(agency_url, data=self.agency_info, headers={'accept': 'application/json', 'Authorization': self.token})
            return response
        except Exception as ex:
            print(
                f"An error occurred while posting the agency information: {str(ex)}")

    
    def get_social_media_links(self, social_media_links, social_media_type):
        return next((social_media_link for social_media_link in social_media_links if social_media_type.lower() in social_media_link.lower()), None)
     


