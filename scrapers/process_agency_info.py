import requests, os, json
from scrapers.social_scraper import SocialScraper
from scrapers.security_scraper import SecurityScraper
from scrapers.accessibility_scraper import AccessibilityScraper
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
                    profile_info[bucket] = securityScraper.get_security_privacy_info(self.website)
                elif bucket == "outreach_and_communication":
                    profile_info[bucket] = socialScraper.get_outreach_communication_info(social_media_info, contact_info)
                elif bucket == "website_accessibility":
                    profile_info[bucket] = accessibilityScraper.get_website_accessibility_info(self.website)


            agency_details = {
                "id": self.agency['id'],
                "name": self.agency['name'],
                "Website": self.website,
                "profile": profile_info
                }

            data_accessor = AgencyDataAccessor(None, self.agency)
            data_accessor.update_scrape_info(agency_details)
            return agency_details
        except Exception as ex:
            print(f"An error occurred while processing the agency information: {str(ex)}")


