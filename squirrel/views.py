from django.shortcuts import render
from .models import Squirrel
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .forms import SquirrelForm

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

def edit(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, unique_squirrel_id=squirrel_id)
    context = {'sighting': squirrel}
    return render(request, 'squirrel/update.html', context)

def update_request(request, sighting_id):
    if request.method == 'POST':
        form = SquirrelForm(request.POST or None)
        
        if form.is_valid():
            #form.save()
            return HttpResponse('Thank you! Your change has been saved.')
        else:
            return HttpResponse('Sorry, your input information is invalid. Check again.')
    else:
        return JsonResponse({}, status=405)



# Create your views here.
