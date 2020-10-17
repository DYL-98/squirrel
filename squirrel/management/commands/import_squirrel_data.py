from django.core.management.base import BaseCommand, CommandError
from squirrel.models import Squirrel
import os
import csv

class Command(BaseCommand):
    help = 'Import the file from the given location (as argument) to the database.'
    
    def add_arguments(self, parsar):
        parsar.add_argument('file_location', help='File Location')
    
    def handle(self, *args, **kwargs):
        file_ = kwargs['file_location']
        
        with open(file_) as fp:
            reader = csv.DictReader(fp)

            for item in reader:
                print(item['X'])

