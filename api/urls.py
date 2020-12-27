# Create your views here.
from . import views
from django.urls import path

urlpatterns=[
    path("laptop-list/", views.laptopList, name='laptop-list'),
    path("laptop-create/",views.laptopCreate, name='laptop-create'),
    path('laptop-update/<str:pk>/',views.laptopUpdate, name='laptop-update'),
    path('laptop-delete/<str:pk>/',views.laptopDelete, name='laptop-delete'),
    path('laptop-detail/<str:pk>/',views.laptopDetail, name='laptop-detail')

]