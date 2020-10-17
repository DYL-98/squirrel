from django.urls import path
from . import views

app_name = 'squirrel'

urlpatterns = [
    path('map/', views.simple, name='map'),
    path('sighting/', views.list_all, name='list_all'),
]
