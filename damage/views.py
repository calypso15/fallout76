from django.shortcuts import render
from django.template import loader

from .models import Weapon


def index(request):
    weapon_list = Weapon.objects.all()
    
    context = {
        'weapon_list': weapon_list,
    }
    
    return render(request, 'damage/index.html', context)
    
def detail(request, weapon_id):
    weapon = Weapon.objects.get(id=weapon_id)
        
    context = {
        'weapon': weapon,
        'weapon_dps': weapon.damage * weapon.speed,
    }

    return render(request, 'damage/detail.html', context)
    
def compare(request, weapon_id1, weapon_id2):
    weapon1 = Weapon.objects.get(id=weapon_id1)
    weapon2 = Weapon.objects.get(id=weapon_id2)
   
    context = {
        'weapon1': weapon1,
        'weapon2': weapon2,
    }

    return render(request, 'damage/compare.html', context)