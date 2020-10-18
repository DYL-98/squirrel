from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    
    latitude = models.FloatField(
        help_text = _('*Required*'),
    )

    longitude = models.FloatField(
        help_text = _('*Required*'),
    )

    unique_squirrel_id = models.CharField(
        max_length = 50,
        help_text = _('*Required*')
    )

    class Shift_choice(models.TextChoices):
        AM = 'AM', _('AM')
        PM = 'PM', _('PM')

    shift = models.CharField(
        max_length = 2,
        help_text =_('*Required*'),
        choices = Shift_choice.choices,
    )

    date = models.DateField(
        help_text = _('*Required. Input as YYYY-mm-dd.*'),
    )

    class Age_choice(models.TextChoices):
        ADULT = 'Adult', _('Adult squirrel')
        JUVENILE = 'Juvenile', _('Juvenile squirrel')

    age = models.CharField(
        max_length = 8,
        help_text = _('Optional'),
        blank = True,
        choices = Age_choice.choices,
    )

    def __str__(self):
        return self.unique_squirrel_id


class UpdateRequest(models.Model):

    squirrel = models.ForeignKey(
            'squirrel.Squirrel',
            on_delete = models.CASCADE
    )

    new_latitude = models.FloatField()
    new_longitude = models.FloatField()
    new_unique_squirrel_id = models.CharField(max_length=50)
    class Shift_choice(models.TextChoices):
        AM = 'AM', _('in the morning')
        PM = 'PM', _('in the afternoon')
    new_shift = models.CharField(
        max_length=2,
        choices = Shift_choice.choices
    )
    new_date = models.DateField()
    class Age_choice(models.TextChoices):
        ADULT = 'Adult', _('Adult squirrel')
        JUVENILE = 'Juvenile', _('Juvenile squirrel')
    new_age = models.CharField(
        max_length = 8,
        blank = True,
        choices = Age_choice.choices
    )
    def __str__(self):
        return f'Squirrel {self.new_unique_squirrel_id} has been updated.'










# Create your models here.
