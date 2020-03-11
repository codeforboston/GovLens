import requests
import logging
from .scrapers.social_scraper import SocialScraper
from .scrapers.security_scraper import SecurityScraper
from .scrapers.accessibility_scraper import AccessibilityScraper
from .agency_dataaccessor import AgencyDataAccessor
from . import settings

logger = logging.getLogger(__name__)


class AgencyInfo:
    def __init__(self, agency):
        self.agency_firms = []
        self.agency = agency
        self.website = agency["website"]
        self.buckets = [
            "security_and_privacy",
            "outreach_and_communication",
            "website_accessibility",
        ]
        self.agency_dataaccessor = AgencyDataAccessor(None, self.agency)

    def process_agency_info(self):
        try:
            # HTTP Get on agency url
            agency_url = self.agency.get("website", None)
            if agency_url is None or agency_url == "":
                logger.error(
                    f"Website url is not available for {self.agency['id']}, name: {self.agency['name']}"
                )
                self.agency_dataaccessor.update_agency_info(self.agency)
                return
            logger.info(f"Scraping the website {agency_url}")
            page = requests.get(agency_url, timeout=30)
            # Initialize scrapers
            socialScraper = SocialScraper(page, agency_url)
            securityScraper = SecurityScraper(page, agency_url)
            accessibilityScraper = AccessibilityScraper(page, agency_url)

            social_media_info, contact_info = socialScraper.scrape_info()
            profile_info = {}

            # Figure out the google_api_key and then fix the below buckets
            for bucket in self.buckets:
                if bucket == "security_and_privacy":
                    if settings.GOOGLE_API_KEY:
                        profile_info[
                            bucket
                        ] = securityScraper.get_security_privacy_info()
                elif bucket == "outreach_and_communication":
                    profile_info[
                        bucket
                    ] = socialScraper.get_outreach_communication_info(
                        social_media_info, contact_info
                    )
                elif bucket == "website_accessibility":
                    if settings.GOOGLE_API_KEY:
                        profile_info[
                            bucket
                        ] = accessibilityScraper.get_website_accessibility_info()

            agency_details = {
                "id": self.agency["id"],
                "name": self.agency["name"],
                "Website": self.website,
                "profile": profile_info,
            }

            self.agency_dataaccessor.enrich_agency_info_with_scrape_info(agency_details)
            return agency_details
        except Exception as ex:
            logger.error(
                ex, "An error occurred while processing the agency information"
            )
