from django.urls import path
from app1.views import studen

urlpatterns=[
    path("register",studen)
    ]