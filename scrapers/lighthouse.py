import os
import requests, json
from django.conf import settings
from scrapers.base_api_client import ApiClient

<<<<<<< HEAD
#GOOGLE_API_KEY = settings.GOOGLE_API_KEY 
=======
GOOGLE_API_KEY = "" #os.environ['GOOGLE_API_KEY']
>>>>>>> 27c64bb8c4c0b3b661f16c6c8830b77d771a46bc
PAGE_INSIGHTS_ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
MOBILE_FRIENDLY_ENDPOINT = "https://search.google.com/test/mobile-friendly" # from what i have tested, very hard to automate

<<<<<<< HEAD
'''
Lighthouse has 5 categories of information that can be pulled from a url
- performance
- accessibility
- best_practices
- pwa proressive web app : relatively fast, mobile friendly, secure origin some best practices 
- seo search engine optimization 
=======
class GoogleMobileFriendlyClient(ApiClient):
    def __init__(self, api_uri=MOBILE_FRIENDLY_ENDPOINT, api_key=GOOGLE_API_KEY):
        ApiClient.__init__(self, api_uri, api_key)
>>>>>>> 27c64bb8c4c0b3b661f16c6c8830b77d771a46bc

    def get_mobile_friendly(self, url):
        data = {
                'url': url
        }
<<<<<<< HEAD
}
'''
def get_lighthouse_results(url,category):
    data = {'url': url, 'category': category}#,'key': GOOGLE_API_KEY}
    response = requests.get(PAGE_INSIGHTS_ENDPOINT,
                            params=data)
    return json.loads(response.content.decode('utf-8'))


# TODO get this to work
def check_mobile_friendly(url):
    data = {
        'url': url
    }
    params = {
        'key': GOOGLE_API_KEY
    } 
    response = requests.post(MOBILE_FRIENDLY_ENDPOINT,
                            params=params, data=data)
    return json.loads(response.content.decode('utf-8'))

=======
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
>>>>>>> 27c64bb8c4c0b3b661f16c6c8830b77d771a46bc
