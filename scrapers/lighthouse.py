from .scrapers.base_api_client import ApiClient
from . import settings


PAGE_INSIGHTS_ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
MOBILE_FRIENDLY_ENDPOINT = "https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run"  # from what i have tested, very hard to automate

"""
Lighthouse has 5 categories of information that can be pulled from a url
- performance
- accessibility
- best_practices
- pwa proressive web app : relatively fast, mobile friendly, secure origin some best practices
- seo search engine optimization """


class PageInsightsClient(ApiClient):
    def __init__(self, api_uri=PAGE_INSIGHTS_ENDPOINT, api_key=settings.GOOGLE_API_KEY):
        ApiClient.__init__(self, api_uri, api_key)

    def get_page_insights(self, url, category):
        data = {"url": url, "key": self.api_key, "category": category}
        return self.get("", data=data)


class GoogleMobileFriendlyClient(ApiClient):
    def __init__(
        self, api_uri=MOBILE_FRIENDLY_ENDPOINT, api_key=settings.GOOGLE_API_KEY
    ):
        self.urls = []
        self.results = []
        ApiClient.__init__(self, api_uri, api_key)

    def get_mobile_friendly(self, url, index):
        data = {"url": url}
        params = {"key": self.api_key}
        return self.post("", index, data=data, params=params)
