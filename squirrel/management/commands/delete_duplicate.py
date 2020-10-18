from django.core.management.base import BaseCommand, CommandError
from squirrel.models import Squirrel
from django.db.models import Min

class Command(BaseCommand):
    def add_arguments(self, parsar):
        parsar.add_argument('file_location', help='File Location')

    def handle(self, *args, **kwargs):
        # First select the min ids
        min_id_objects = Squirrel.objects.values('unique_squirrel_id').annotate(minid=Min('id'))
        min_ids = [obj['minid'] for obj in min_id_objects]
        # Now delete
        Squirrel.objects.exclude(id__in=min_ids).delete()
