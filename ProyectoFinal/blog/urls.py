from django.urls import path
from blog import views
from .views import Inicio, postDetails
from django.contrib.auth.views import LogoutView
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    # path('', views.inicio, name='inicio'),
    path('', Inicio.as_view(), name='inicio'),
    path('<slug:slug>/', postDetails.as_view(), name='post-details'),
    path('about', views.about, name='about'),
    path('crear-post', views.creaPost, name='creapost'),
    path('buscarPost', views.buscarPost, name='buscarPost'),
    path('resultadoBuscar', views.buscar, name = 'resultadoBusqueda'),
    path('login', views.login_request, name = 'login'),
    path('signup', views.register, name = 'signup'),
    path('logout', LogoutView.as_view(template_name = 'blog/logout.html'), name = 'logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)