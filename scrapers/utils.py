import requests, json

GOOGLE_API_KEY = "AIzaSyC25WRU_Vgdu0YF4_ePhg1WHVg5AQUCpRE"
PAGE_INSIGHTS_ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
MOBILE_FRIENDLY_ENDPOINT = "https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run"


def check_site_performance(url):
    data = {'url': url, 'key': GOOGLE_API_KEY}
    response = requests.get(PAGE_INSIGHTS_ENDPOINT,
                                  params=data)
    return json.loads(response.content.decode('utf-8'))


def check_mobile_friendly(url):
    data = {
        'url': url,
        'key': GOOGLE_API_KEY,
    }
    response = requests.get(MOBILE_FRIENDLY_ENDPOINT,
                            params=data)
    return json.loads(response.content.decode('utf-8'))