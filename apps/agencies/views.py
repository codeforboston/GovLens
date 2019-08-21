from django.views import generic
from .models import Agency


class AgencyListView(generic.ListView):
    context_object_name = 'agencies'
    paginate_by = 25

    def get_queryset(self):
        return Agency.objects.order_by('name')


class AgencyView(generic.DetailView):
    model = Agency

    def get_context_data(self, **kwargs):
        context = super(AgencyView, self).get_context_data(**kwargs)
        agency = context['object']
        context['last_entry'] = agency.entry_set.last()
        return context
