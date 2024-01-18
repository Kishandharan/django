from django.shortcuts import render

def home(request):
    f1=open("time_table.txt","r")
    info1=f1.readlines()
    
    return render(request,'classes/index.html',{'param1':info1})
