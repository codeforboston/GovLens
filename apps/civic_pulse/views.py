from django.views import generic
from .models import Agency


class AgencyListView(generic.ListView):
    template_name = 'agency-list.html'
    context_object_name = 'agencies'
    paginate_by = 25

    def get_queryset(self):
        return Agency.objects.order_by('created_date')


class AgencyView(generic.DetailView):
    model = Agency
    template_name = 'agency-detail.html'

    def get_context_data(self, **kwargs):
        context = super(AgencyView, self).get_context_data(**kwargs)
        agency = context['object']
        context['last_entry'] = agency.entry_set.last()
        return context

class HomeView(generic.ListView):
    template_name = 'home.html'
    model = Agency

    # def get_context_data(self, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     agency = context['object']
    #     context['last_entry'] = agency.entry_set.last()
    #     return context

    def get_queryset(self):
        return Agency.objects.order_by('created_date')
