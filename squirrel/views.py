from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
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
    if request.method == 'POST':
        form = SquirrelForm(request.POST or None)
        if form.is_valid():
            # Do somthing
            squirrel.latitude = form.cleaned_data['latitude']
            squirrel.longitude = form.cleaned_data['longitude']
            squirrel.unique_squirrel_id = form.cleaned_data['unique_squirrel_id']
            squirrel.date = form.cleaned_data['date']
            squirrel.shift = form.cleaned_data['shift']
            squirrel.age= form.cleaned_data['age']
            squirrel.save()
            return HttpResponse('Thank you! Your change has been saved.')
        else:
            return HttpResponse('Sorry! Your input format is invalid. Please check again.')
    else:
        form = SquirrelForm()
        context = {'sighting': squirrel, 'form': form}
        return render(request, 'squirrel/update.html', context)

def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST or None)
        if form.is_valid():
            obj = Squirrel()
            obj.latitude = form.cleaned_data['latitude']
            obj.longitude = form.cleaned_data['longitude']
            obj.unique_squirrel_id = form.cleaned_data['unique_squirrel_id']
            obj.date = form.cleaned_data['date']
            obj.shift = form.cleaned_data['shift']
            obj.age = form.cleaned_data['age']
            # duplicate check
            if Squirrel.objects.filter(unique_squirrel_id = form.cleaned_data['unique_squirrel_id']).exists():  
             # redirect to edit page
                this_squirrel = get_object_or_404(Squirrel, unique_squirrel_id = form.cleaned_data['unique_squirrel_id'])
                form = SquirrelForm()
                context = {'sighting': this_squirrel, 'form': form}
                return HttpResponse('Oops, it looks like the Unique Squirrel ID you entered already exists. Try using edit function~')
            else:
                obj.save()
                return HttpResponse('Thank you! New sighting has been added!')
        else:
            return HttpResponse('Sorry! Your input format is invalid. Please check again!')
    else:
        form = SquirrelForm()
        context = {'form': form}
        return render(request, 'squirrel/add.html', context)



