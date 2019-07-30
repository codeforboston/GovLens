import requests, json
from django.conf import settings

#GOOGLE_API_KEY = settings.GOOGLE_API_KEY 
PAGE_INSIGHTS_ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
MOBILE_FRIENDLY_ENDPOINT = "https://search.google.com/test/mobile-friendly" # from what i have tested, very hard to automate

'''
Lighthouse has 5 categories of information that can be pulled from a url
- performance
- accessibility
- best_practices
- pwa proressive web app : relatively fast, mobile friendly, secure origin some best practices 
- seo search engine optimization 

The score for each category is in the JSON results as..
{
  'lighthouseResult': {
        'categories': {
            '<category name>': {
                'score': Int
            }
        }
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

