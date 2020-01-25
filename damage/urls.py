from django.urls import path

from . import views

urlpatterns = [
	# ex: /
    path('', views.index, name='index'),
    
    # ex: /detail/5/
    path('detail/<int:weapon_id>/', views.detail, name='detail'),
    
    # ex: /5/results/
    path('compare/<int:weapon_id_1>/<int:weapon_id_2>/', views.compare, name='compare'),
]