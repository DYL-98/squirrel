from django.urls import path
from . import views

app_name = 'squirrel'

urlpatterns = [
    path('map/', views.simple, name='map'),
    path('sightings/', views.list_all, name='list_all'),
    path('sightings/add/', views.add, name='add'),
    path('sightings/stats/', views.stats, name='stats'),
    path('sightings/<str:squirrel_id>/', views.edit, name='edit'),
]
