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

    def get_context_data(self, **kwargs):
        context = super(AgencyView, self).get_context_data(**kwargs)
        agency = context['object']
        context['last_entry'] = agency.entry_set.last()
        return context

