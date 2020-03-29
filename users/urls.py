from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
	#default auth url
	path('', include('django.contrib.auth.urls')),
	#registration page
	path('register/', views.register, name='register'),
]
