from django.conf.urls import patterns, include, url
from django.contrib import admin
from gestion import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view()),
    url(r'^login/', views.LoginView.as_view()),
    url(r'^dispensar-receta/(?P<receta_id>.+)', views.DispensarRecetaView.as_view()),
    url(r'^modificar-receta/(?P<receta_id>.+)', views.ModificarRecetaView.as_view()),
    url(r'^buscar-paciente-farmaceutico/', views.BuscarPacienteFarmaceuticoView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}),
    url(r'^buscar-paciente/', views.BuscarPacienteView.as_view()),

)
