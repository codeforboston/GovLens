import requests, os, json
from .base_scraper import BaseScraper
from agency_dataaccessor import AgencyDataAccessor

class SecurityScraper(BaseScraper):

    def __init__(self, raw_page_content, url, lighthouse_pwa, page):
        self.page = raw_page_content
        self.url = url
        self.lighthouse_pwa = lighthouse_pwa
        self.page = page

    def get_security_privacy_info(self):
        return {
            "https": SecurityScraper.get_http_acess(self),
            "hsts": SecurityScraper.get_hsts(self),
            "privacy_policies": SecurityScraper.get_privacy_policies(self)
        }

    def get_http_acess(self):
        #return self.get_criteria_object(None, "https" in url)
        try: 
            #response = get_lighthouse_results(self.website,'pwa')
            score = self.lighthouse_pwa['lighthouseResult']['audits']['is-on-https']['score']  
            is_criteria_met = True if score == 1 else False 
            return self.get_criteria_object(score, is_criteria_met)      
        except:
            print("Error in get_http_acess for", self.url)

    def get_hsts(self):
        #return self.get_criteria_object(None, "strict-transport-security" in requests.get(self.url, timeout = 30))
        try: 
            #response = get_lighthouse_results(self.website,'pwa')
            score = self.lighthouse_pwa['lighthouseResult']['audits']['redirects-http']['score']  
            is_criteria_met = True if score == 1 else False 
            return self.get_criteria_object(score, is_criteria_met)      
        except:
            print("Error in get_hsts for", self.url)

    def get_privacy_policies(self):
        is_criteria_met = True if "privacy policy" in self.page.text.lower() else False
        return self.get_criteria_object(None, is_criteria_met)
        
