import requests, os, json
from .base_scraper import BaseScraper
from agency_dataaccessor import AgencyDataAccessor
from .base_api_client import ApiClient
from lighthouse import GoogleMobileFriendlyClient

class AccessibilityScraper(BaseScraper):

    def __init__(self, raw_page_content, url):
        self.raw_page_content = raw_page_content
        self.url = url
        self.apiClient = GoogleMobileFriendlyClient()

    #TODO: get real metrics instead of random values
    def get_website_accessibility_info(self,url):
        return {
            "mobile_friendly": self.check_mobile_friendly(url),
            "page_speed": self.get_random_value("page_speed"),
            "performance": self.get_site_performance(url),
            "multi_lingual": self.get_random_value("multi_lingual")
        }

    def get_site_performance(self, url):
        print("hello world")
        # response = get_lighthouse_results(url,'performance')
        # score = response['lighthouseResult']['categories']['performance']['score']
        # is_criteria_met = True if score >= 80 else False
        # return self.get_criteria_object(score, is_criteria_met)

    def check_mobile_friendly(self, url):
        response = self.apiClient.get_mobile_friendly(url)
        isMobileFriendly = False

        if(response.ok()):
            isMobileFriendly = True if response.content['mobileFriendliness'] == 'MOBILE_FRIENDLY' else False
            if(not isMobileFriendly):
                #TODO: return issues as well if site is not mobile friendly
                mobileFriendlyIssues = response.content['mobileFriendlyIssues']
        return isMobileFriendly





