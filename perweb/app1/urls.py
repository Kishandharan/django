from django.urls import path
from app1.views import home, home1, home2
urlpatterns = [
	path('login', home),
    path('signup',home1),
    path('any',home2)]