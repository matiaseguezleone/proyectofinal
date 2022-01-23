from django.urls import path
from blog import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about', views.about, name='about'),
    path('crear-post', views.creaPost, name='creapost'),
    path('buscarPost', views.buscarPost, name='buscarPost'),
    path('resultadoBuscar', views.buscar, name = 'resultadoBusqueda')
]