from django.conf.urls import patterns, include, url
from django.contrib import admin
from gestion import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view()),
    url(r'^login/', views.LoginView.as_view()),
    url(r'^nueva-receta/', views.NuevaRecetaView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}),

)
