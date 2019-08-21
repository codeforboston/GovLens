from rest_framework import viewsets
from apps.agencies.api.serializers import AgencySerializer,EntrySerializer
from apps.agencies.models import Agency, Entry


class AgencyViewSet(viewsets.ModelViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer