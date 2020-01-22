from rest_framework import viewsets
from apps.civic_pulse.api.serializers import AgencySerializer, EntrySerializer
from apps.civic_pulse.models import Agency, Entry


class AgencyViewSet(viewsets.ModelViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
