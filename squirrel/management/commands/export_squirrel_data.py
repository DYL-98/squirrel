from django.core.management.base import BaseCommand, CommandError
from squirrel.models import Squirrel
import os
import csv
from datetime import datetime
from djqscsv import write_csv

class Command(BaseCommand):
    help = 'Export the data from the database to the given location (as argument).'

    def add_arguments(self, parsar):
        parsar.add_argument('file_location', help='File Location')

    def handle(self, *args, **kwargs):
        path = kwargs['file_location']
        
        all_entries = Squirrel.objects.all()
        
        with open(path, 'wb') as csv_file:
            write_csv(all_entries, csv_file)

        msg = f'You have successfully exported data to {path}.'
        self.stdout.write(self.style.SUCCESS(msg))
