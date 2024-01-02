from django.urls import path
from holiday1.views import holiday
urlpatterns = [
    path('',holiday)
]
