from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from app1.forms import inputdat, inputdat1
from app1.models import mode1

def home(request):
    if request.method=="POST":
        form1=inputdat(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            gmail=data1.get("gmail")
            psw=data1.get("psw")
            message=""
            try:
                id=mode1.objects.get(gmail=gmail,password=psw)
                return redirect('/app1/any')
            except ObjectDoesNotExist:
                message="invalid gmail or password"
                return render(request,"app1/index.html",{"param1":message,"form":form1})
    else:
        form1=inputdat()
    return render(request,"app1/index.html",{"form":form1})

def home1(request):
    if request.method=="POST":
        form1=inputdat1(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            name=data.get("name")
            gmail=data.get("gmail")
            psw=data.get("psw")
            psw1=data.get("psw1")
            message=""
            if psw==psw1:
                try:
                    a=mode1.objects.get(gmail=gmail)
                    if a==gmail:
                        message=gmail
                    else:
                        mode1.objects.create(name=name,gmail=gmail,password=psw1)
                        return redirect('/app1/login')
                except:
                    message=gmail
            else:
                message="does not match"
            return render(request,"app1/index1.html",{"param1":message,"form":form1})
    else:
        form1=inputdat1()
    return render(request,"app1/index1.html",{"form":form1})

def home2(request):
    return render(request,"app1/index3.html")