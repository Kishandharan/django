from django.urls import path
from app1.views import sign_in,sign_up
urlpatterns = [
	path('up', sign_up),path('in', sign_in)]