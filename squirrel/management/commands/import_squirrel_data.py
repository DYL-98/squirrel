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

            for item in reader:
                obj = Squirrel()
                obj.latitude = item['X']
                obj.longitude = item['Y']
                obj.unique_squirrel_id = item['Unique Squirrel ID']
                obj.date = datetime.strptime(item['Date'],'%m%d%Y')
                obj.shift = item['Shift']
                obj.age = item['Age']
                obj.save()

        msg = f'You have successfully imported data from {file_}.'
        self.stdout.write(self.style.SUCCESS(msg))

