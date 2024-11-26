from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path('libros/', views.Listlibros.as_view(), name="libros"),
    path('libros2/', views.Listlibros2.as_view(), name="libros2"),
    path('libros-detalle/<pk>/', views.LibroDetailView.as_view(), name="libro-detalle"),
]

