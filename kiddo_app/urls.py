from . import views
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView


urlpatterns = [
    #path('', views.app_homepage, name='app_homepage'),
    path('', index, name='index'),
    #path('about_us', views.about_us, name='about_us'),
    path('about_us', TemplateView.as_view(template_name='aboutUs.html'), name='about_us'), 
    path('services', views.services, name='services'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('register/', views.register, name = 'register'),
    path('registrarcliente', views.registrar_cliente, name = 'registrarcliente'),
    path('signin', CustomLoginView.as_view(template_name='signin.html'), name = 'signin'),
    path('loggedin', views.loggedin, name = 'loggedin'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    path('registrarpais', views.pais, name = 'registrarpais'),
    path('registrartienda', views.tienda, name = 'registrartienda'),
    path('registrarevento', views.evento, name = 'registrarevento'),
    path('registrados', views.registrados, name = 'registrados'),
    path('eventosagendados', views.eventosagendados, name = 'eventosagendados'),
    path('tiendas_registradas', views.tiendas_registradas, name = 'tiendasregistradas'),
    path('paises_registrados', views.paises_registrados, name = 'paisesregistrados'),
    path('buscarTienda', views.buscar_tienda, name = 'buscarTienda'),
    path('user_data', views.UserListView.as_view(), name = 'listaUsuarios'),
    path('user_detail/<int:pk>/', views.UserDetailView.as_view(template_name='user_detail.html'), name = 'detalleUsuarios'),
    path('user_create/', views.UserCreateView.as_view(template_name='user_create.html'), name = 'crearUsuarios'),
    path('user_update/<int:pk>/', views.UserUpdateView.as_view(template_name='user_create.html'), name = 'updateUsuarios'),
    path('user_delete/<int:pk>/', views.UserDeleteView.as_view(template_name='user_confirm_delete.html'), name = 'deleteUsuarios'),
    path('login/', views.UserDeleteView.as_view(template_name='user_confirm_delete.html'), name = 'login'),
]
