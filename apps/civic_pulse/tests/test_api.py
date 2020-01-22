import json
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from apps.civic_pulse.models import Agency, Entry


class AgencyAPITest(TestCase):
    def setUp(self):
        Agency.objects.create(name="Test Agency 1")
        Agency.objects.create(name="Test Agency 2")
        self.client = APIClient()

    def test_GET(self):
        response = self.client.get("/api/agencies/")
        self.assertEqual(200, response.status_code)

        agencies_json = json.loads(response.content.decode("utf-8"))
        expected_results = [
            {
                "id": 1,
                "name": "Test Agency 1",
                "website": "",
                "twitter": "",
                "facebook": "",
                "phone_number": "",
                "address": "",
                "description": "",
                "last_successful_scrape": None,
                "scrape_counter": 0,
            },
            {
                "id": 2,
                "name": "Test Agency 2",
                "website": "",
                "twitter": "",
                "facebook": "",
                "phone_number": "",
                "address": "",
                "description": "",
                "last_successful_scrape": None,
                "scrape_counter": 0,
            },
        ]
        self.assertEqual(agencies_json, expected_results)

    def test_GET_Individual(self):
        response = self.client.get("/api/agencies/1/")
        self.assertEqual(200, response.status_code)

        agency_json = json.loads(response.content.decode("utf-8"))
        expected_results = {
            "id": 1,
            "name": "Test Agency 1",
            "website": "",
            "twitter": "",
            "facebook": "",
            "phone_number": "",
            "address": "",
            "description": "",
            "last_successful_scrape": None,
            "scrape_counter": 0,
        }
        self.assertEqual(agency_json, expected_results)

    def test_POST_Unauthorized(self):
        data = {"name": "Test POST Agency"}
        response = self.client.post("/api/agencies/", data=data, format="json")
        self.assertEqual(401, response.status_code)

        json_response = json.loads(response.content.decode("utf-8"))
        self.assertEqual(
            "Authentication credentials were not provided.", json_response["detail"]
        )

    def test_POST_Authorized(self):
        user = User.objects.create_user(
            username="test", email="test@test.test", password="test"
        )
        token = Token.objects.create(user=user)

        data = {"id": 5, "name": "Test POST Agency"}

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response = self.client.post("/api/agencies/", data=data, format="json")
        self.assertEqual(201, response.status_code)

        json_response = json.loads(response.content.decode("utf-8"))
        expected_results = {
            "id": 5,
            "name": "Test POST Agency",
            "website": "",
            "twitter": "",
            "facebook": "",
            "phone_number": "",
            "address": "",
            "description": "",
            "last_successful_scrape": None,
            "scrape_counter": 0,
        }

        self.assertEqual(json_response, expected_results)


class EntryAPITest(TestCase):
    def setUp(self):
        self.agency = Agency.objects.create(name="Test Agency 1", id=1)
        Entry.objects.create(agency_id=self.agency.id,)
        Entry.objects.create(
            agency_id=self.agency.id, https_enabled=True,
        )

        self.client = APIClient()

    def test_GET(self):
        response = self.client.get("/api/entries/")
        self.assertEqual(200, response.status_code)

        entries_json = json.loads(response.content.decode("utf-8"))
        expected_results = [
            {
                "id": 1,
                "agency": 1,
                "https_enabled": False,
                "has_privacy_policy": False,
                "mobile_friendly": False,
                "good_performance": False,
                "has_social_media": False,
                "has_contact_info": False,
            },
            {
                "id": 2,
                "agency": 1,
                "https_enabled": True,
                "has_privacy_policy": False,
                "mobile_friendly": False,
                "good_performance": False,
                "has_social_media": False,
                "has_contact_info": False,
            },
        ]

        self.assertEqual(entries_json, expected_results)

    def test_GET_Individual(self):
        response = self.client.get("/api/entries/1/")
        self.assertEqual(200, response.status_code)

        entry_json = json.loads(response.content.decode("utf-8"))
        expected_results = {
            "id": 1,
            "agency": 1,
            "https_enabled": False,
            "has_privacy_policy": False,
            "mobile_friendly": False,
            "good_performance": False,
            "has_social_media": False,
            "has_contact_info": False,
        }

        self.assertEqual(entry_json, expected_results)

    def test_POST_Unauthorized(self):
        data = {
            "agency": 1,
            "https_enabled": True,
            "has_privacy_policy": False,
            "mobile_friendly": False,
            "good_performance": False,
            "has_social_media": True,
            "has_contact_info": False,
        }
        response = self.client.post("/api/entries/", data=data, format="json")
        self.assertEqual(401, response.status_code)

        json_response = json.loads(response.content.decode("utf-8"))
        self.assertEqual(
            "Authentication credentials were not provided.", json_response["detail"]
        )

    def test_POST_Authorized(self):
        user = User.objects.create_user(
            username="test", email="test@test.test", password="test"
        )
        token = Token.objects.create(user=user)

        data = {
            "agency": 1,
            "https_enabled": True,
            "has_privacy_policy": False,
            "mobile_friendly": False,
            "good_performance": False,
            "has_social_media": True,
            "has_contact_info": False,
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response = self.client.post("/api/entries/", data=data, format="json")
        self.assertEqual(201, response.status_code)

        json_response = json.loads(response.content.decode("utf-8"))
        expected_results = {
            "id": 3,
            "agency": 1,
            "https_enabled": True,
            "has_privacy_policy": False,
            "mobile_friendly": False,
            "good_performance": False,
            "has_social_media": True,
            "has_contact_info": False,
        }
        self.assertEqual(json_response, expected_results)
