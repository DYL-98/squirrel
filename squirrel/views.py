from django.shortcuts import render
from .models import Squirrel
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def simple(request):
    sightings = Squirrel.objects.values('latitude', 'longitude')[:100]
    context = {'sightings':sightings}
    return render(request, 'squirrel/map_.html', context)

def list_all(request):
    all_sightings = Squirrel.objects.values('id', 'unique_squirrel_id', 'date')
    context = {'sightings': all_sightings}
    return render(request, 'squirrel/list_all.html', context)

def show_detail(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, pk=squirrel_id)
    context = {'sighting': squirrel}
    return render(request, 'squirrel/detail.html', context)



# Create your views here.
