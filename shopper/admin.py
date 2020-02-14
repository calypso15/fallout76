from django.contrib import admin

from .models import Location, Recipe, Ingredient, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    extras = 1
    inlines = (RecipeIngredientInline,)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Location)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)