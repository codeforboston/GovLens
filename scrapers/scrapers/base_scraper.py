import requests, os, json
from agency_dataaccessor import AgencyDataAccessor

class BaseScraper:

    def __init__(self, raw_page_content, url):
        self.raw_page_content = raw_page_content
        self.url = url

    def get_random_value(self, url):
                return self.get_criteria_object(None, True)

    def get_criteria_object(self, criteria, is_met):
            return {
                 "met_criteria" : is_met,
                 "info": criteria
             }





