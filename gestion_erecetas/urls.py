from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from gestion import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gestion_erecetas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.IndexView.as_view()),
    url(r'^admin/', include(admin.site.urls)),

)
