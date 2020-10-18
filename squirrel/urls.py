from django.urls import path
from . import views

app_name = 'squirrel'

urlpatterns = [
    path('map/', views.simple, name='map'),
    path('sightings/', views.list_all, name='list_all'),
    path('details/<int:squirrel_id>/', views.show_detail, name='details'),
    path('sightings/<str:squirrel_id>/', views.edit, name='edit'),
    path('update_request/<int:sighting_id>', views.update_request, name='update_request'),
]
