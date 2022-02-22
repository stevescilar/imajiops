from django.urls import path
from . import views

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('client/<str:pk>/', views.client , name = "client"),
]