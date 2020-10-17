from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    
    latitude = models.FloatField(
        help_text = _('The latitude of the squirrel being seen.'),
    )

    longitude = models.FloatField(
        help_text = _('The longitude of the squirrel being seen.'),
    )

    unique_squirrel_id = models.CharField(
        max_length = 50,
        help_text = _('The unique ID of this squirrel.')
    )

    class Shift_choice(models.TextChoices):
        AM = 'AM', _('in the morning')
        PM = 'PM', _('in the afternoon')

    shift = models.CharField(
        max_length = 2,
        choices = Shift_choice.choices,
    )

    date = models.DateField(
        help_text = _('The date that the squirrel was seen.'),
    )

    class Age_choice(models.TextChoices):
        ADULT = 'Adult', _('Adult squirrel')
        JUVENILE = 'Juvenile', _('Juvenile squirrel')

    age = models.CharField(
        max_length = 8,
        help_text = _('The age group of the squirrel.'),
        blank = True,
        choices = Age_choice.choices,
    )

    def __str__(self):
        return self.unique_squirrel_id










# Create your models here.
