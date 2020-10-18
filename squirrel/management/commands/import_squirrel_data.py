from django.db.models import Min
from django.core.management.base import BaseCommand, CommandError
from squirrel.models import Squirrel
import os
import csv
from datetime import datetime

class Command(BaseCommand):
    help = 'Import the file from the given location (as argument) to the database.'
    
    def add_arguments(self, parsar):
        parsar.add_argument('file_location', help='File Location')
    
    def handle(self, *args, **kwargs):
        file_ = kwargs['file_location']
        
        with open(file_) as fp:
            reader = csv.DictReader(fp)
            
            # delete all existing records
            Squirrel.objects.all().delete()

            # Insert from data
            for item in reader:
                obj = Squirrel()
                obj.longitude = item['X']
                obj.latitude = item['Y']
                obj.unique_squirrel_id = item['Unique Squirrel ID']
                obj.date = datetime.strptime(item['Date'],'%m%d%Y')
                obj.shift = item['Shift']
                obj.age = item['Age']
                obj.save()

        # delete sightings with duplicate unique_squirrel_id
        min_id_objects = Squirrel.objects.values('unique_squirrel_id').annotate(minid=Min('id'))
        min_ids = [obj['minid'] for obj in min_id_objects]
        # Now delete
        Squirrel.objects.exclude(id__in=min_ids).delete()

        msg = f'You have successfully imported data from {file_}.Duplicate has also been deleted.'
        self.stdout.write(self.style.SUCCESS(msg))

