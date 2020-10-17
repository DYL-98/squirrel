from django.shortcuts import render
from .models import Squirrel
from django.http import JsonResponse


def simple(request):
    sightings = Squirrel.objects.values('latitude', 'longitude')[:100]
    context = {'sightings':sightings}
    return render(request, 'squirrel/map_.html', context)



# Create your views here.
