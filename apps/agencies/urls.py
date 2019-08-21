from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.AgencyListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$',views.AgencyDetailView.as_view(),name='detail'),
]
