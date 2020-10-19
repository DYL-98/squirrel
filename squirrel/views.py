from django.db.models import Min, Max
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Squirrel
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .forms import SquirrelForm
import datetime

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
            if squirrel.unique_squirrel_id == form.cleaned_data['unique_squirrel_id']:
                return HttpResponse('Oops, it looks like the Unique Squirrel ID you entered is occupied by another cute little squirrel!')
            else:
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

def stats(request):
    all_sightings_qry = Squirrel.objects.all()
    
    # Stats of interest
    north_most = 90
    south_most = -90
    east_most = -60
    west_most = -90
    shift_mode = ""
    month_mode = ""
    age_mode = ""

    # extreme location
    lat_dict = all_sightings_qry.aggregate(max_lat = Max('latitude'), min_lat = Min('latitude'))
    long_dict = all_sightings_qry.aggregate(max_long = Max('longitude'), min_long = Min('longitude'))
    north_most = lat_dict['max_lat']
    south_most = lat_dict['min_lat']
    west_most = -1*float(long_dict['min_long'])
    east_most = -1*float(long_dict['max_long'])

    # shift mode
    count_AM = all_sightings_qry.filter(shift='AM').count()
    count_PM = all_sightings_qry.filter(shift='PM').count()
    if count_AM >= count_PM:
        shift_mode = "0:00-11:59 AM"
    else:
        shift_mode = "12:00-11:59 PM"

    # Month mode
    all_dates = list(all_sightings_qry.values('date'))
    all_dates = [item['date'].strftime("%B") for item in all_dates]
    month_mode = max(set(all_dates), key=all_dates.count)

    # Age mode
    count_adult = all_sightings_qry.filter(age="Adult").count()
    count_juvenile = all_sightings_qry.filter(age="Juvenile").count()
    age_mode = ("Adult" if count_adult >= count_juvenile else "Juvenile")

    context = {
        "north_most": north_most,
        "south_most": south_most,
        "west_most": west_most,
        "east_most": east_most,
        "shift_mode": shift_mode,
        "month_mode": month_mode,
        "age_mode": age_mode,
    }

    return render(request, 'squirrel/stats.html', context)




