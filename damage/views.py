from .models import Weapon

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world.")
	
def detail(request, weapon_id):
	results = Weapon.objects.filter(id=weapon_id)
	
	if(len(results) == 0):
		return HttpResponse("No matches.")
	
	if(len(results) > 1):
		return HttpResponse("Multiple matches.")
		
	weapon = results[0]
	
	return HttpResponse(f"{ weapon.name } (level { weapon.level }). { weapon.damage * weapon.speed } DPS.")
	
def compare(request, weapon_id_1, weapon_id_2):
	return HttpResponse(f"You're are comparing weapons { weapon_id_1 } and { weapon_id_2 }.")