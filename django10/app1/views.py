from os import name
from django.shortcuts import render
from app1.models import student

from app1.forms import studentform # Create your views here.
def studen(request):
    a1=student.objects.all()
    a=a1[0].name
    if request.method=="POST":
        form1=studentform(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request , "app1/index.html",{"form":form1,"list1":a})
    else:
        form1=studentform()
    return render(request,"app1/index.html",{"form":form1,"list1":a})
