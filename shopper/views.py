from django.shortcuts import render
from django.template import loader

from .models import Recipe


def index(request):
    recipe_list = Recipe.objects.all()
    
    context = {
        'recipe_list': recipe_list,
    }
    
    return render(request, 'shopper/index.html', context)