from django.urls import path

from . import views

urlpatterns = [
	# ex: /
    path('', views.index, name='index'),
    
    # ex: /5/results/
    path('<int:weapon_id>/', views.detail, name='detail'),
]