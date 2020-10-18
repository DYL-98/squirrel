from django.forms import ModelForm
from .models import Squirrel

class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields =[
        'latitude',
        'longitude',
        'unique_squirrel_id',
        'date',
        'shift',
        'age',
        ]
