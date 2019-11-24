"""civic_pulse_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from apps.civic_pulse.api.viewsets import *
from apps.civic_pulse.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register(r'entries', EntryViewSet)
router.register(r'agencies', AgencyViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
#    url(r'^$', AgencyListView.as_view(), name='index'),
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^agency/(?P<pk>[0-9]+)/$',AgencyView.as_view(),name='agency-detail'),
]

urlpatterns += staticfiles_urlpatterns()
