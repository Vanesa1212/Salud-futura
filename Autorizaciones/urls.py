from django.urls import path
from . import views

urlpatterns = [
    path('autorizaciones/', views.listar_autorizaciones, name='listar_autorizaciones'),
    path('autorizaciones/crear/', views.crear_autorizacion, name='crear_autorizacion'),
    path('autorizaciones/editar/<int:pk>/', views.editar_autorizacion, name='editar_autorizacion'),
    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('pacientes/crear/', views.crear_pacientes, name='crear_pacientes'),
    path('pacientes/editar/<int:pk>/', views.editar_pacientes, name='editar_pacientes'),
]