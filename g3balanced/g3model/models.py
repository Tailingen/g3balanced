from django.db import models
from .resourses import *

class BalanceUnit(models.Model):
    balance = models.CharField(choices=BALANCES, default='vanil', max_length=255)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    note = models.TextField()

class Weapon(BalanceUnit):
    weapontype = models.CharField(choices=WEAPONS, max_length=255)
    damagetype = models.CharField(choices=DAMAGES, max_length=255)
    damagevalue = models.IntegerField()
    effect = models.CharField(choices=EFFEXTS, max_length=255)
    damagerange = models.IntegerField()
    requirement = models.TextField()
    bonus = models.TextField()

class Missile(BalanceUnit):
    missletype = models.CharField(choices=MISSILES, max_length=255)
    damagetype = models.CharField(choices=DAMAGES, max_length=255)
    damagevalue = models.IntegerField()
    effect = models.CharField(choices=EFFEXTS, max_length=255)

class Armor(BalanceUnit):
    armortype = models.CharField(choices=ARMORS, max_length=255)
    deftype = models.CharField(choices=DEFS, max_length=255)
    defvalue = models.IntegerField()
    requirement = models.TextField()
    bonus = models.TextField()

class Consumable(BalanceUnit):
    consumtype = models.CharField(choices=CONSUMABLES, max_length=255)
    bonustype1 = models.CharField(choices=BONUSES, max_length=255)
    bonusvalue1 = models.IntegerField()
    bonustype2 = models.CharField(choices=BONUSES, max_length=255)
    bonusvalue2 = models.IntegerField()
    bonustype3 = models.CharField(choices=BONUSES, max_length=255)
    bonusvalue3 = models.IntegerField()
    bonustype4 = models.CharField(choices=BONUSES, max_length=255)
    bonusvalue4 = models.IntegerField()

class Scroll(BalanceUnit):
    magic = models.CharField(max_length=255)
    manacost = models.IntegerField()
    damagetype = models.CharField(choices=DAMAGES, max_length=255)
    damagevalue = models.IntegerField()
    effect = models.CharField(choices=EFFEXTS, max_length=255)
    impact = models.TextField()

class Miscleanous(BalanceUnit):
    misctype = models.CharField(choices=MISCS, max_length=255)

class Recipe(BalanceUnit):
    recipetype = models.CharField(choices=RECIPS, max_length=255)
    result = models.CharField(max_length=255)
    resultamount = models.IntegerField()

class Skill(BalanceUnit):
    skilltype = models.CharField(choices=SKILLS, max_length=255)
    requirement = models.TextField()
    atributtype1 = models.CharField(choices=BONUSES, max_length=255)
    atributvalue1 = models.IntegerField()
    atributtype2 = models.CharField(choices=BONUSES, max_length=255)
    atributvalue2 = models.IntegerField()
    atributtype3 = models.CharField(choices=BONUSES, max_length=255)
    atributvalue3 = models.IntegerField()
    atributtype4 = models.CharField(choices=BONUSES, max_length=255)
    atributvalue4 = models.IntegerField()
    bonus = models.TextField()

class Spell(BalanceUnit):
    spelltype = models.CharField(choices=SPELLS, max_length=255)
    requirement = models.TextField()
    atributtype1 = models.CharField(choices=BONUSES, max_length=255)
    atributvalue1 = models.IntegerField()
    atributtype2 = models.CharField(choices=BONUSES, max_length=255)
    atributvalue2 = models.IntegerField()
    atributtype3 = models.CharField(choices=BONUSES, max_length=255)
    atributvalue3 = models.IntegerField()
    atributtype4 = models.CharField(choices=BONUSES, max_length=255)
    atributvalue4 = models.IntegerField()
    manacost = models.IntegerField()
    damagetype = models.CharField(choices=DAMAGES, max_length=255)
    damagevalue = models.IntegerField()
    effect = models.CharField(choices=EFFEXTS, max_length=255)
    impact = models.TextField()

class Transform(BalanceUnit):
    transformtype = models.CharField(choices=TRANSFORMS, max_length=255)
    unit = models.TextField()
    manacost = models.IntegerField()
