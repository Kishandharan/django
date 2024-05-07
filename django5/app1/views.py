from django.shortcuts import render

from app1.forms import inputweb
def home(request):
    if request.method=="POST":
        form1=inputweb(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            n=data1.get("num1")
            fact1=factorial1(n)
            return render(request,'app1/index.html',{'param1':fact1,"form":form1})
    else:
        form1=inputweb()
    return render(request,'app1/index.html',{"form":form1})

def factorial1(n):
    fact1=1
    for i in range(n,0,-1):
        fact1=fact1*i
    return fact1
