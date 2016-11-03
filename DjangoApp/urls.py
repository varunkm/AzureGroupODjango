"""
Definition of urls for DjangoApp.
"""

from datetime import datetime
from django.conf.urls import url
from app.forms import BootstrapAuthenticationForm
from app.views import *
from app import views
from app.models import *
from django.contrib.auth.views import *


# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
  url(r'^$', views.CitationsList.as_view(), name='citation_list'),
  url(r'^citations/$', views.CitationsList.as_view(), name='citation_list'),
  url(r'^new/$', views.CitationCreate.as_view(), name='citation_new'),
  url(r'^edit/(?P<pk>\d+)$', views.CitationUpdate.as_view(), name='citation_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.CitationDelete.as_view(), name='citation_delete'),
  url(r'^login/$',
    login, {'template_name': 'app/login.html'}
),
  url(r'^logout/$',
    logout, {'next_page': '/login/'}
),
  url('^register/', CreateView.as_view(
            template_name='app/register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
    url(r'^admin/', admin.site.urls),
]
