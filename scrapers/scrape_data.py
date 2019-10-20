import csv, os
import json

from process_agency_info import AgencyInfo

# The Scheduler will invoke this function. Parameter is list of agencies for which the data needs to be scraped
def scrape_data(agencies):
    if len(agencies) <= 0:
        print("No Agency information was passed to scrape")
        return

    for agency in agencies:
        agency_instance = AgencyInfo(agency)
        agency_instance.process_agency_info()
