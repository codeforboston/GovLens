import requests, os, json
from .base_scraper import BaseScraper
from agency_dataaccessor import AgencyDataAccessor

class SecurityScraper(BaseScraper):

    def __init__(self, raw_page_content, url):
        self.bucket = []
        self.raw_page_content = raw_page_content
        self.url = url

    def get_security_privacy_info(self, url):
            return {
                "https": self.get_http_acess(url),
                "privacy_policies": self.get_random_value("comprehensive")
            }

    def get_http_acess(self, url):
            return self.get_criteria_object(None, "https" in url)


