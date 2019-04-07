from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import *


class AgencyListView(generic.ListView):
    template_name = 'agency-list.html'
    context_object_name = 'agencies'
    paginate_by = 25

    def get_queryset(self):
        return Agency.objects.order_by('name')


class AgencyView(generic.DetailView):
    model = Agency
    template_name = 'agency-detail.html'

