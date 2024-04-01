from django import forms
from django.core.exceptions import ValidationError
from .models import *

class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = ['balance', 'name', 'price', 'note', 'weapontype', 'damagetype', 'damagevalue', 'effect', 'damagerange', 'requirement', 'bonus']