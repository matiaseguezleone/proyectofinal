from ast import Delete
from django.urls import path, include
from blog import views
from .views import Inicio, deletePost, postDetails, creaPost, updatePost
from django.contrib.auth.views import LogoutView
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    # path('', views.inicio, name='inicio'),
    # path('', include('blog.urls')),
    path('', Inicio.as_view(), name='inicio'),
    path('<slug:slug>/', postDetails.as_view(), name='post-details'),
    path('about', views.about, name='about'),
    path('crear-post', views.creaPost, name='creapost'),
    path('buscarPost', views.buscarPost, name='buscarPost'),
    path('resultadoBuscar', views.buscar, name = 'resultadoBusqueda'),
    path('<slug:slug>/editar', updatePost.as_view(), name = 'editarPost'),
    path('<slug:slug>/borrar', deletePost.as_view(), name = 'borrarPost')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)