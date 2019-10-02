from django.views import generic

from .models import Agency

class AgencyListView(generic.ListView):
    template_name = 'agency-list.html'
    context_object_name = 'agencies'
    paginate_by = 25


    def get_queryset(self):
        return Agency.objects.order_by('created_date')

class AgencyResults(generic.ListView):
    model = Agency
    #form = AgencyForm'
    context_object_name = 'agencies'
    template_name = 'agency-list.html'

    paginate_by = 25

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Agency.objects.filter(name__icontains=query)
        return queryset

class AgencyView(generic.DetailView):
    model = Agency
    template_name = 'agency-detail.html'

    def get_context_data(self, **kwargs):
        context = super(AgencyView, self).get_context_data(**kwargs)
        agency = context['object']
        context['last_entry'] = agency.entry_set.last()
        return context
