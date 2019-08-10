import os
import requests, json
from django.conf import settings
from scrapers.base_api_client import ApiClient

GOOGLE_API_KEY = "AIzaSyCJOEyfcXBfnLt3dpaUAD78Pp8XfIbGSx0" #os.environ['GOOGLE_API_KEY']
PAGE_INSIGHTS_ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
MOBILE_FRIENDLY_ENDPOINT = "https://search.google.com/test/mobile-friendly" # from what i have tested, very hard to automate

'''
Lighthouse has 5 categories of information that can be pulled from a url
- performance
- accessibility
- best_practices
- pwa proressive web app : relatively fast, mobile friendly, secure origin some best practices
- seo search engine optimization '''


class PageInsightsClient(ApiClient):
    def __init__(self, api_uri=PAGE_INSIGHTS_ENDPOINT, api_key=GOOGLE_API_KEY):
        ApiClient.__init__(self, api_uri, api_key)

    def get_page_insights(self, url):
        data = {
                'url': url,
                'key': self.api_key
        }
        return self.get("", data=data)


if __name__=="__main__":
    google_client = PageInsightsClient(PAGE_INSIGHTS_ENDPOINT, GOOGLE_API_KEY)
    data = {'url':"https://stackoverflow.com/questions/24022558/differences-between-staticfiles-dir-static-root-and-media-root"}
    params = {'key':google_client.api_key}

    response = google_client.get_page_insights("https://github.com/codeforboston/civicpulse/pull/50/commits/98f1c32bd3e8798d0fe3d47f68d05744c47ff275")
    print("CHECKED")


