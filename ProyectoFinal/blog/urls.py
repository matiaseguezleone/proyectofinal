from django.urls import path
from blog import views
from .views import Inicio, postDetails


urlpatterns = [
    # path('', views.inicio, name='inicio'),
    path('', Inicio.as_view(), name='inicio'),
    path('post/<int:pk>', postDetails.as_view(), name='post-details'),
    path('about', views.about, name='about'),
    path('crear-post', views.creaPost, name='creapost'),
    path('buscarPost', views.buscarPost, name='buscarPost'),
    path('resultadoBuscar', views.buscar, name = 'resultadoBusqueda')
]