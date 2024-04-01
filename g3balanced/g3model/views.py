from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .forms import WeaponForm
from .models import Weapon
from django.urls import reverse_lazy

class WeaponList(ListView):
    model = Weapon
    ordering = 'damagevalue'
    template_name = 'weapons.html'
    context_object_name = 'weapons'

class WeaponCreate(CreateView):
    form_class = WeaponForm
    model = Weapon
    template_name = 'weapon_edit.html'
    success_url = reverse_lazy('weapon_list')
