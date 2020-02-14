from django.urls import path

from . import views

app_name = 'damage'

urlpatterns = [
	# ex: /
    path('', views.index, name='index'),
    
    # ex: /detail/5/
    path('detail/<int:weapon_id>/', views.detail, name='detail'),
    
    # ex: /5/results/
    path('compare/<int:weapon_id1>/<int:weapon_id2>/', views.compare, name='compare'),
]