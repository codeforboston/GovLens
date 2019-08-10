import requests, os, json
from .base_scraper import BaseScraper
from agency_dataaccessor import AgencyDataAccessor
from .base_api_client import ApiClient
from lighthouse import lighthouse_scraper

class AccessibilityScraper(BaseScraper):

    def __init__(self, raw_page_content, url, lighthouse_performance, lighthouse_pwa, page):
        self.page = raw_page_content
        self.url = url
        #self.apiClient = lighthouse_scraper()
        self.lighthouse_performance = lighthouse_performance
        self.lighthouse_pwa = lighthouse_pwa
        self.page = page

    def get_website_accessibility_info(self):
        return {
            "mobile_friendly": AccessibilityScraper.get_mobile_friendliness(self), #use either lighthouse or https://www.google.com/webmasters/tools/mobile-friendly/?url=<website_addr>
            "page_speed": AccessibilityScraper.get_page_speed(self),
            "performance": AccessibilityScraper.get_site_performance(self),
            "multi_lingual": AccessibilityScraper.get_multi_lingual(self)
        }

    def get_multi_lingual(self):
        is_criteria_met = True if (("translate" or "select language" or "select-language" in self.page.text.lower()) 
        or ("espanol" or "Espa&ntilde;ol") in self.page.a) else False
        return self.get_criteria_object(None, is_criteria_met)
    
    def get_site_performance(self):
        try:
            #response = get_lighthouse_results(url,'performance')
            score = self.lighthouse_performance['lighthouseResult']['categories']['performance']['score']
            is_criteria_met = True if score*100 >= 80 else False # the score in the Json file is a percentage
            return self.get_criteria_object(score, is_criteria_met)
        except:
            print("Error in get_site_performance for", self.url)

    def get_mobile_friendliness(self):
        try:
            #response = get_lighthouse_results(url,'pwa')
            score = self.lighthouse_pwa['lighthouseResult']['audits']['content-width']['score']#If the width of your app's content doesn't match the width of the viewport, your app might not be optimized for mobile screens.
            title = self.lighthouse_pwa['lighthouseResult']['audits']['content-width']['title']
            is_criteria_met = True if title == 'Content is sized correctly for the viewport' else False
            return self.get_criteria_object(score, is_criteria_met)
        except:
            print("Error in get_mobile_friendliness for", self.url)       
        """response = self.apiClient.get_mobile_friendly(url)
        isMobileFriendly = False

        if(response.ok()):
            isMobileFriendly = True if response.content['mobileFriendliness'] == 'MOBILE_FRIENDLY' else False
            if(not isMobileFriendly):
                #TODO: return issues as well if site is not mobile friendly
                mobileFriendlyIssues = response.content['mobileFriendlyIssues']
        return isMobileFriendly"""

    def get_page_speed(self):
        try:
            #response = get_lighthouse_results(url,'performance')
            score = self.lighthouse_performance['lighthouseResult']['audits']['speed-index']['score'] 
            """ note: several page speed metrics can be obbtained and are slightly different. Example
            response['lighthouseResult']['audits']['speed-index']['displayValue'] contains the time in seconds and not a score
            speed-index in response['lighthouseResult']['categories']['performance']['auditRefs'] """
            is_criteria_met = True if score*100 >= 80 else False # the score in the Json file is a percentage
            return self.get_criteria_object(score, is_criteria_met)
        except:
            print("Error in get_page_speed for", self.url)
