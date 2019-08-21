from django.test import TestCase, Client
from django.urls import reverse
from ..models import Agency, Entry


class AgencyListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.agency = Agency.objects.create(name='Test Agency',id=1)

    @property
    def url(self):
        return reverse('index')

    def test_GET(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)

    def test_agency(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.context['agencies']),1)
        self.assertEqual(response.context['agencies'][0].name,self.agency.name)

    def test_search(self):
        response = self.client.get(self.url,data={'q': self.agency.name})
        self.assertEqual(len(response.context['agencies']), 1)

        response = self.client.get(self.url,data={'q': 'Something Else'})
        self.assertEqual(len(response.context['agencies']), 0)


class AgencyDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.agency = Agency.objects.create(name='Test Agency',id=1)

    @property
    def url(self):
        return reverse('agencies:detail',kwargs={'pk': self.agency.id})

    def test_GET(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)

    def test_agency(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context['agency'].name,self.agency.name)

    def test_last_entry(self):
        Entry.objects.create(agency=self.agency,https_enabled=True)
        response = self.client.get(self.url)
        self.assertTrue(response.context['last_entry'].https_enabled)