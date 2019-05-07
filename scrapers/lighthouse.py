import requests, json
from django.conf import settings

GOOGLE_API_KEY = settings.GOOGLE_API_KEY
PAGE_INSIGHTS_ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
MOBILE_FRIENDLY_ENDPOINT = "https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run"

'''
Lighthouse has 5 categories of information that can be pulled from a url
- performance
- accessibility
- best_practices
- pwa
- seo

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
    data = {'url': url, 'key': GOOGLE_API_KEY, 'category': category}
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


# print(check_mobile_friendly('http://www.mass.gov/cgly/'))