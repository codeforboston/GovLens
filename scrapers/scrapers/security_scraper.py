import requests, os, json
from .base_scraper import BaseScraper
from agency_dataaccessor import AgencyDataAccessor
from lighthouse import PageInsightsClient


class SecurityScraper(BaseScraper):

    def __init__(self, raw_page_content, url):
        self.page = raw_page_content
        self.url = url
        self.apiClient = PageInsightsClient()

    def get_security_privacy_info(self):
        return {
            "https": self.get_http_acess(),
            "hsts": self.get_hsts(),
            "privacy_policies": self.get_privacy_policies()
        }

    def get_http_acess(self):
        try:
            lighthouse_results = self.apiClient.get_page_insights(self.url, 'pwa').content['lighthouseResult']
            score = lighthouse_results['audits']['is-on-https']['score']
            is_criteria_met = True if score == 1 else False
            return self.get_criteria_object(score, is_criteria_met)
        except:
            print("Error in get_http_acess for", self.url)

    def get_hsts(self):
        try:
            lighthouse_results = self.apiClient.get_page_insights(self.url, 'pwa').content['lighthouseResult']
            score = lighthouse_results['audits']['redirects-http']['score']
            is_criteria_met = True if score == 1 else False
            return self.get_criteria_object(score, is_criteria_met)
        except:
            print("Error in get_hsts for", self.url)

    def get_privacy_policies(self):
        is_criteria_met = True if "privacy policy" in self.page.text.lower() else False
        return self.get_criteria_object(None, is_criteria_met)

