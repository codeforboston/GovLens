import logging

import requests

from . import settings

logger = logging.getLogger(__name__)


class AgencyApiService:
    def __init__(self):
        self.base_url = settings.GOVLENS_API_ENDPOINT

    def get_all_agencies(self):
        try:
            all_agency_list = self._get(self.base_url)
            return all_agency_list
        except Exception as ex:
            logger.error(ex, "Error while retrieving all the agency information")

    def _get(self, url):
        response = requests.get(
            url,
            headers={
                "Content-type": "application/json",
                "Authorization": "Token {}".format(settings.GOVLENS_API_TOKEN),
            },
        )
        response.raise_for_status()
        return response.json()
