import os
import requests, json
from django.conf import settings
from scrapers.base_api_client import ApiClient

GOOGLE_API_KEY = "" #os.environ['GOOGLE_API_KEY']
PAGE_INSIGHTS_ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
MOBILE_FRIENDLY_ENDPOINT = "https://search.google.com/test/mobile-friendly" # from what i have tested, very hard to automate

'''
Lighthouse has 5 categories of information that can be pulled from a url
- performance
- accessibility
- best_practices
- pwa proressive web app : relatively fast, mobile friendly, secure origin some best practices 
- seo search engine optimization '''

def get_lighthouse_results(url,category):
    data = {'url': url, 'category': category}#,'key': GOOGLE_API_KEY}
    response = requests.get(PAGE_INSIGHTS_ENDPOINT,
                            params=data)
    return json.loads(response.content.decode('utf-8'))

class lighthouse_scraper(ApiClient):
    def __init__(self, api_uri=MOBILE_FRIENDLY_ENDPOINT, api_key=GOOGLE_API_KEY):
        ApiClient.__init__(self, api_uri, api_key)

    def get_mobile_friendly(self, url):
        data = {
                'url': url
        }
        params = {
                'key': self.api_key
        }
        return self.post("", data=data, params=params)

if __name__=="__main__":
    google_client = ApiClient(MOBILE_FRIENDLY_ENDPOINT, GOOGLE_API_KEY)
    data = {'url':"https://stackoverflow.com/questions/24022558/differences-between-staticfiles-dir-static-root-and-media-root"}
    params = {'key':google_client.api_key}

    response = google_client.post("", data=data, params=params)
    print("CHECKED")


