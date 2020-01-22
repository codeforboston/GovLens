from rest_framework import serializers
from apps.civic_pulse.models import Agency, Entry


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = [
            "id",
            "name",
            "website",
            "twitter",
            "facebook",
            "phone_number",
            "address",
            "description",
            "last_successful_scrape",
            "scrape_counter",
            "notes",
        ]


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = [
            "id",
            "agency",
            "https_enabled",
            "has_privacy_policy",
            "mobile_friendly",
            "good_performance",
            "has_social_media",
            "has_contact_info",
            "notes",
        ]
