from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('usuarios/crear', views.crear, name='crear'),
    path('usuarios/eliminar/<int:id>',views.eliminar, name='eliminar'),
    path('usuarios/editar/<int:id>',views.editar, name='editar'),
    path('mk/', views.mk, name='mk'),
    path('documentacion',views.documentacion, name='documentacion'),
    
]
