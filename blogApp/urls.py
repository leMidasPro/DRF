from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('Getallpost/', views.Getallpost),
    path('Createpost/', views.Createpost),
    path('deletepost/', views.deletepost),
    path('Getpost/', views.Getpost),
    path('Updatepost/', views.Updatepost),
]