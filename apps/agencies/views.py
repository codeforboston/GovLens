from django.views import generic
from .models import Agency
from .viewmixins import SearchMixin


class AgencyListView(SearchMixin,generic.ListView):
    model = Agency
    context_object_name = 'agencies'
    paginate_by = 25
    search_fields = ['name']
    ordering = 'name'



class AgencyView(generic.DetailView):
    model = Agency

    def get_context_data(self, **kwargs):
        context = super(AgencyView, self).get_context_data(**kwargs)
        agency = context['object']
        context['last_entry'] = agency.entry_set.last()
        return context
