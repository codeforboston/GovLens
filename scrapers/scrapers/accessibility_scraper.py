from .base_scraper import BaseScraper
from agency_dataaccessor import AgencyDataAccessor
from .base_api_client import ApiClient
from lighthouse import PageInsightsClient

class AccessibilityScraper(BaseScraper):

    def __init__(self, raw_page_content, url):
        self.page = raw_page_content
        self.url = url
        self.apiClient = PageInsightsClient()

    def get_website_accessibility_info(self):
        return {
            "mobile_friendly": self.get_mobile_friendliness(),
            "page_speed": self.get_page_speed(),
            "performance": self.get_site_performance(),
            "multi_lingual": self.get_multi_lingual()
        }

    def get_multi_lingual(self):
        is_criteria_met = True if (("translate" or "select language" or "select-language" in self.page.text.lower())
        or ("espanol" or "Espa&ntilde;ol") in self.page.a) else False
        return self.get_criteria_object(None, is_criteria_met)

    def get_site_performance(self):
        try:
            lighthouse_results = self.apiClient.get_page_insights(self.url, 'performance').content['lighthouseResult']
            performanceResults = lighthouse_results['categories']['performance']['score']
            is_criteria_met = True if performanceResults*100 >= 80 else False # the score in the Json file is a percentage
            return self.get_criteria_object(performanceResults, is_criteria_met)
        except:
            print("Error in get_site_performance for", self.url)

    def get_mobile_friendliness(self):
        try:
            lighthouse_results = self.apiClient.get_page_insights(self.url, 'pwa').content['lighthouseResult']
            #If the width of your app's content doesn't match the width of the viewport, your app might not be optimized for mobile screens.
            score = lighthouse_results['audits']['content-width']['score']
            title = lighthouse_results['audits']['content-width']['title']
            is_criteria_met = True if title == 'Content is sized correctly for the viewport' else False
            return self.get_criteria_object(score, is_criteria_met)
        except:
            print("Error in get_mobile_friendliness for", self.url)

    def get_page_speed(self):
        try:
            lighthouse_results = self.apiClient.get_page_insights(self.url, 'performance').content['lighthouseResult']
            speed_index = lighthouse_results['audits']['speed-index']['score']
            is_criteria_met = True if speed_index*100 >= 80 else False # the score in the Json file is a percentage
            return self.get_criteria_object(speed_index, is_criteria_met)
        except:
            print("Error in get_page_speed for", self.url)
