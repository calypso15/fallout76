from django.urls import path

from . import views

app_name = 'shopper'

urlpatterns = [
	# ex: /
    path('', views.index, name='index'),
]