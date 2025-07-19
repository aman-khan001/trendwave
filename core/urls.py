from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:pk>/', views.details, name='details'),
    path('search/', views.search, name='search'),
]

