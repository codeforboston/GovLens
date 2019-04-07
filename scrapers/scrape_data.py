
import requests
import os, decimal, simplejson
from bs4 import BeautifulSoup
import re

class ScrapeSocialInfo:

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
            
            if contact_us_link:
                if "http" in contact_us_link["href"]:
                    print("making an extra call to get the contact info")
                    contact_us_page = requests.get(contact_us_link["href"])
                else:
                    print("making an extra call to get the contact info")
                    contact_us_page = requests.get(self.url+contact_us_link["href"])
                contact_us_soup = BeautifulSoup(contact_us_page.content,'html.parser')
                contact_info = self.get_contact_info(contact_us_soup)
            else:
                print("not making an extra call to get the contact info")
                contact_info = self.get_contact_info(soup)
        except Exception as ex:
            print(f"An error occurred while processing the social media information: {str(ex)}")

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
                    emails = ScrapeSocialInfo.email_regex.findall(contact_us_str) if not emails else emails
                    phone_numbers = ScrapeSocialInfo.phone_regex.findall(contact_us_str) if not phone_numbers else phone_numbers
                    address = ScrapeSocialInfo.address_regex.findall(contact_us_str) if not address else address

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
            print(f"An error occurred while extracting the contact information for the firm {self.url}: {str(ex)}")
            return None