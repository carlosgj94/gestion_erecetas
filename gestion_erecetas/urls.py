from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from gestion import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view()),
    url(r'^admin/', include(admin.site.urls)),

)
