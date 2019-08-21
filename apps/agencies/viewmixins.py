from django.db.models import Q


class SearchMixin:
    search_fields = []

    @property
    def search_term(self):
        return self.request.GET.get("q",'')

    def get_queryset(self):
        qs = super(SearchMixin, self).get_queryset()

        if self.search_term and self.search_fields:
            search_fields_icontains = [field + '__icontains' for field in self.search_fields]
            q_fields = Q()
            for field in search_fields_icontains:
                q_fields.add(Q(**{field: self.search_term}), Q.OR)
            return qs.filter(q_fields)

        return qs