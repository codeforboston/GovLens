import requests
from bs4 import BeautifulSoup
from .base_scraper import BaseScraper
import re

class SocialScraper(BaseScraper):

    phone_regex = re.compile(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})")
    email_regex = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}")
    address_regex = re.compile(r"\s\d{1,5} [a-zA-Z0-9\s\.,]+[A-Z]{2}[\s\-\s]{0,3}[0-9]{5,6}?[,]*")

    def __init__(self, raw_page_content, url):
        self.raw_content = raw_page_content
        self.url = url

    def scrape_info(self):
        soup = BeautifulSoup(self.raw_content.content, 'html.parser')
        social_media_criteria = ["twitter.com", "facebook.com", "instagram.com","youtube.com","linkedin.com"]
        a_tags = soup.findAll("a", href=True)
        social_media_links = []
        contact_us_link = ""
        try:
            for tag in a_tags:
                try:
                    href_link = tag.get("href", None)
                    if href_link is not None:
                        if "contact" in tag.text.lower():
                            contact_us_link = tag
                        elif any(link in tag["href"] for link in social_media_criteria):
                            social_media_links.append(tag["href"])
                except Exception as ex:
                    print(f"An error occurred while trying to extract the social media information: {str(ex)}")
                    logging.error(f"An error occurred while trying to extract the social media information: {str(ex)}")
            if contact_us_link:
                if "http" in contact_us_link["href"]:
                    print(f"making an extra call to get the contact info: {contact_us_link['href']}")
                    contact_us_page = requests.get(contact_us_link["href"])
                else:
                    print(f"making an extra call to get the contact info: {self.url+contact_us_link['href']}")
                    contact_us_page = requests.get(self.url+contact_us_link["href"])
                contact_us_soup = BeautifulSoup(contact_us_page.content,'html.parser')
                contact_info = self.get_contact_info(contact_us_soup)
            else:
                print("not making an extra call to get the contact info")
                contact_info = self.get_contact_info(soup)
        except Exception as ex:
            print(f"An error occurred while processing the social media information: {str(ex)}")
            logging.error(f"An error occurred while processing the social media information: {str(ex)}")

        return social_media_links, contact_info

    def get_contact_info(self,soup):
        try:
            contact_us_all_elements = soup.findAll()
            contact_us_str = ""
            emails = []
            phone_numbers =[]
            address=[]
            for element in contact_us_all_elements:
                if "contact" in element.text.lower():
                    contact_us_str = element.text.replace('\n',' ')
                    contact_us_str = re.sub('<[^<]+?>', '', contact_us_str)
                    emails = SocialScraper.email_regex.findall(contact_us_str) if not emails else emails
                    phone_numbers = SocialScraper.phone_regex.findall(contact_us_str) if not phone_numbers else phone_numbers
                    address = SocialScraper.address_regex.findall(contact_us_str) if not address else address

            all_contact_info = {}
            if contact_us_str:
                all_contact_info = {
                    "email": list(set(emails)),
                    "phone_number": list(set(phone_numbers)),
                    "address": list(set(address))[0] if address else []
                }
            else:
                print("Contact Information not available")
                all_contact_info = {
                    "email": [],
                    "phone_number": [],
                    "address": []
                }
            return all_contact_info
        except Exception as ex:
            print("An error occurred while extracting the contact information for the firm {self.url}: {str(ex)}")
            logging.error("An error occurred while extracting the contact information for the firm {self.url}: {str(ex)}")
            return None

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
        return self.get_criteria_object(contact_info, is_contact_info_available)

    def get_socialmedia_access(self, social_media_info):
        is_criteria_met = True if social_media_info and len(social_media_info) > 0 else False
        return self.get_criteria_object(social_media_info, is_criteria_met)
