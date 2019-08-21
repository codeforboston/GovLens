from django.views.generic import ListView,DetailView
from .models import Agency


class AgencyListView(ListView):
    model = Agency
    template_name = 'agencies/agency_list.html'
    context_object_name = 'agencies'
    ordering = 'name'
    paginate_by = 25

    @property
    def search_term(self):
        return self.request.GET.get('q')

    def get_queryset(self):
        qs = super(AgencyListView,self).get_queryset()
        if self.search_term:
            qs = qs.filter(name__icontains=self.search_term)
        return qs


class AgencyDetailView(DetailView):
    model = Agency
    template_name = 'agencies/agency_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AgencyDetailView, self).get_context_data(**kwargs)
        context['last_entry'] = self.object.entry_set.last()
        return context
