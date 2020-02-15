from django.db import models

class Location(models.Model):
	name = models.CharField(max_length=64)
	description = models.CharField(blank=True, max_length=128)
	coord_x = models.IntegerField()
	coord_y = models.IntegerField()
	
	def __str__(self):
		return f"{self.name} ({self.coord_x}, {self.coord_y})"
	
class Ingredient(models.Model):
	name = models.CharField(max_length=64)
	
	def __str__(self):
		return f"{self.name}"
	
class Recipe(models.Model):
	name = models.CharField(max_length=64)
	level = models.PositiveSmallIntegerField()
	location = models.ManyToManyField(Location)
	ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient', through_fields=('recipe', 'ingredient'))

	def __str__(self):
		return f"{self.name} (Level {self.level})"
		
class RecipeIngredient(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	count = models.PositiveSmallIntegerField()
	
	def __str__(self):
		return f"{self.recipe} - {self.ingredient} ({self.count})"