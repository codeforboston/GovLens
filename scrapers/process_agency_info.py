import requests, os, json
<<<<<<< HEAD
from scrape_social_info import ScrapeSocialInfo
from lighthouse import get_lighthouse_results
=======
from scrapers.social_scraper import SocialScraper
from scrapers.security_scraper import SecurityScraper
from scrapers.accessibility_scraper import AccessibilityScraper
>>>>>>> 27c64bb8c4c0b3b661f16c6c8830b77d771a46bc
from agency_dataaccessor import AgencyDataAccessor

class AgencyInfo:

    def __init__(self, agency):
        self.agency_firms = []
        self.agency = agency
        self.website = agency['website']
        self.buckets = ["security_and_privacy","outreach_and_communication","website_accessibility"]

    def process_agency_info(self):
        try:
            # HTTP Get on agency url
            agency_url = self.agency.get('website',None)
            if agency_url is None or agency_url == '':
                print(f"Website url is not available for {self.agency['id']}, name: {self.agency['name']}")
                return
            print(f"Scraping the website {agency_url}")

            page = requests.get(agency_url, timeout=30)

            # Initialize scrapers
            socialScraper = SocialScraper(page, agency_url)
            securityScraper = SecurityScraper(page, agency_url)
            accessibilityScraper = AccessibilityScraper(page, agency_url)

            social_media_info, contact_info = socialScraper.scrape_info()
            profile_info = {}

            for bucket in self.buckets:
                if bucket == "security_and_privacy":
<<<<<<< HEAD
                    profile_info[bucket] = self.get_security_privacy_info(self.website, page)
=======
                    profile_info[bucket] = securityScraper.get_security_privacy_info(self.website)
>>>>>>> 27c64bb8c4c0b3b661f16c6c8830b77d771a46bc
                elif bucket == "outreach_and_communication":
                    profile_info[bucket] = socialScraper.get_outreach_communication_info(social_media_info, contact_info)
                elif bucket == "website_accessibility":
<<<<<<< HEAD
                    profile_info[bucket] = self.get_website_accessibility_info(self.website, page)
    
                agency_details = {
                     "id": self.agency['id'],
                     "name": self.agency['name'],
                     "Website": self.website,
                     "profile": profile_info
=======
                    profile_info[bucket] = accessibilityScraper.get_website_accessibility_info(self.website)


            agency_details = {
                "id": self.agency['id'],
                "name": self.agency['name'],
                "Website": self.website,
                "profile": profile_info
>>>>>>> 27c64bb8c4c0b3b661f16c6c8830b77d771a46bc
                }

            data_accessor = AgencyDataAccessor(None, self.agency)
            data_accessor.update_scrape_info(agency_details)
            return agency_details
        except Exception as ex:
<<<<<<< HEAD
            print(f"An error occurred in process_agency_info : {str(ex)}")
    

    
    def get_security_privacy_info(self, url, page):
        return {
            "https": self.get_http_acess(self.website),
            "hsts": self.get_hsts(page),
            "privacy_policies": self.get_privacy_policies(page)
        }

    def get_website_accessibility_info(self,url,page):
        return {
            "mobile_friendly": self.get_mobile_friendliness(url), #use either lighthouse or https://www.google.com/webmasters/tools/mobile-friendly/?url=<website_addr>
            "page_speed": self.get_page_speed(url),
            "performance": self.get_site_performance(url),
            "multi_lingual": self.get_multi_lingual(page)
        }
    
    def get_outreach_communication_info(self, social_media_info, contact_info):
        agency_info = {
            "social_media_access": self.get_socialmedia_access(social_media_info),
            "contact_access": self.get_contact_access(contact_info)
        }
        return agency_info

    def get_contact_access(self, contact_info):
        is_contact_info_available = False
        if contact_info and contact_info["phone_number"] or contact_info["email"] or contact_info["address"]:
            is_contact_info_available = True
        else:
            is_contact_info_available = False
        return self.get_criteria_object(contact_info, is_contact_info_available)
    
    def get_socialmedia_access(self, social_media_info):
        is_criteria_met = True if social_media_info and len(social_media_info) > 0 else False
        return self.get_criteria_object(social_media_info, is_criteria_met)
    
    def get_http_acess(self, url):
        #return self.get_criteria_object(None, "https" in url)
        try: 
            response = get_lighthouse_results(self.website,'pwa')
            score = response['lighthouseResult']['audits']['is-on-https']['score']  
            is_criteria_met = True if score == 1 else False 
            return self.get_criteria_object(score, is_criteria_met)      
        except:
            print("Error in get_http_acess for", self.website)

    def get_hsts(self, page):
        #return self.get_criteria_object(None, "strict-transport-security" in requests.get(self.url, timeout = 30))
        try: 
            response = get_lighthouse_results(self.website,'pwa')
            score = response['lighthouseResult']['audits']['redirects-http']['score']  
            is_criteria_met = True if score == 1 else False 
            return self.get_criteria_object(score, is_criteria_met)      
        except:
            print("Error in get_hsts for", self.website)

    def get_privacy_policies(self, page):
        is_criteria_met = True if "privacy policy" in page.text.lower() else False
        return self.get_criteria_object(None, is_criteria_met)

    def get_multi_lingual(self, page):
        is_criteria_met = True if (("translate" or "select language" or "select-language" in page.text.lower()) 
        or ("espanol" or "Espa&ntilde;ol") in page.a) else False
        return self.get_criteria_object(None, is_criteria_met)

    def get_random_value(self, url):
        return self.get_criteria_object(None, True)

    def get_site_performance(self, url):
        try:
            response = get_lighthouse_results(url,'performance')
            score = response['lighthouseResult']['categories']['performance']['score']
            is_criteria_met = True if score*100 >= 80 else False # the score in the Json file is a percentage
            return self.get_criteria_object(score, is_criteria_met)
        except:
            print("Error in get_site_performance for", url)

    def get_mobile_friendliness(self, url):
        try:
            response = get_lighthouse_results(url,'pwa')
            score = response['lighthouseResult']['audits']['content-width']['score']#If the width of your app's content doesn't match the width of the viewport, your app might not be optimized for mobile screens.
            title = response['lighthouseResult']['audits']['content-width']['title']
            is_criteria_met = True if title == 'Content is sized correctly for the viewport' else False
            return self.get_criteria_object(score, is_criteria_met)
        except:
            print("Error in get_mobile_friendliness for", url)

    def get_page_speed(self, url):
        try:
            response = get_lighthouse_results(url,'performance')
            score = response['lighthouseResult']['audits']['speed-index']['score'] 
            """ note: several page speed metrics can be obbtained and are slightly different. Example
            response['lighthouseResult']['audits']['speed-index']['displayValue'] contains the time in seconds and not a score
            speed-index in response['lighthouseResult']['categories']['performance']['auditRefs'] """
            is_criteria_met = True if score*100 >= 80 else False # the score in the Json file is a percentage
            return self.get_criteria_object(score, is_criteria_met)
        except:
            print("Error in get_page_speed for", url)

    def get_criteria_object(self, criteria, is_met):
        return {
             "met_criteria" : is_met,
             "info": criteria
         }
=======
            print(f"An error occurred while processing the agency information: {str(ex)}")
>>>>>>> 27c64bb8c4c0b3b661f16c6c8830b77d771a46bc


