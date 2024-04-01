from django.urls import path
from .views import WeaponList, WeaponCreate

urlpatterns = [
   path('', WeaponList.as_view(), name='weapon_list'),
   path('create/', WeaponCreate.as_view(), name='weapon_create'),
]