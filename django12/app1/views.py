from django.shortcuts import render
import random as rm
def home(request):
    a="1"
    b="9"
    n=3
    for i in range(n-1):
        a+="0"
        b+="9"
    a=rm.randint(int(a),int(b))
    return render(request,'app1/index.html',{'param1':a})