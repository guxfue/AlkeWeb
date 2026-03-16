from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('amenazas/', views.amenazas, name='amenazas'),
    path('consejos/', views.consejos, name='consejos'),
    path('0x4c4f47494e/', views.easter_egg, name='easter_egg'),
]
