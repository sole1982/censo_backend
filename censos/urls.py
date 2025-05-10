from django.urls import path
from . import views

urlpatterns = [
    path('censos/', views.crear_censo, name='crear_censo'),
]