from django.views.generic import ListView,DetailView
from .models import Agency


class AgencyListView(ListView):
    model = Agency
    template_name = 'agencies/agency_list.html'
    context_object_name = 'agencies'
    ordering = 'name'
    paginate_by = 25

    def get_queryset(self):
        qs = super(AgencyListView,self).get_queryset()
        self.search_term = self.request.GET.get('q','')
        if self.search_term:
            qs = qs.filter(name__icontains=self.search_term)
        return qs


class AgencyView(DetailView):
    model = Agency
    template_name = 'agencies/agency_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AgencyView, self).get_context_data(**kwargs)
        agency = context['object']
        context['last_entry'] = agency.entry_set.last()
        return context
