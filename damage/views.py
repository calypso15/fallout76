from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")
    
def detail(request, weapon_id):
    return HttpResponse(f"You're looking at weapon { weapon_id }.")
    
def compare(request, weapon_id_1, weapon_id_2):
    return HttpResponse(f"You're are comparing weapons { weapon_id_1 } and { weapon_id_2 }.")