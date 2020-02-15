from django.contrib import admin

from .models import Location, Recipe, Ingredient, RecipeIngredient

class LocationAdmin(admin.ModelAdmin):
    ordering = ['name']

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    ordering = ['name']
    inlines = (RecipeIngredientInline,)
    extras = 1
    
class IngredientAdmin(admin.ModelAdmin):
    ordering = ['name']
    
class RecipeIngredientAdmin(admin.ModelAdmin):
    ordering = ('recipe', 'ingredient')

admin.site.register(Location, LocationAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)