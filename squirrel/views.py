from django.shortcuts import render
from .models import Squirrel
from django.http import JsonResponse


def simple(request):
    sightings = Squirrel.objects.values('latitude', 'longitude')[:100]
    context = {'sightings':sightings}
    return render(request, 'squirrel/map_.html', context)

def list_all(request):
    all_sightings = Squirrel.objects.values('unique_squirrel_id', 'date')
    context = {'sightings': all_sightings}
    return render(request, 'squirrel/list_all.html', context)



# Create your views here.
