import os
dproject=input("Enter the django project name")
dapp=input("Enter the django app name")
os.chdir(dproject)
os.chdir(f"../{dproject}/{dproject}")
f1=open("settings.py","r+")
info1=f1.read()
list1=[]
a=info1.replace("'django.contrib.staticfiles',","'django.contrib.staticfiles',\n\t'app1'")
f1.seek(0)
f1.write(a)
f1.close()

f1=open("urls.py","w")
f1.write(f"""from django.urls import path
from {dapp}.views import home
urlpatterns = [path('', home),]""")
f1.close()

os.chdir(f".././{dapp}")
f1=open("views.py","w")
any="""from django.shortcuts import render
def home(request):
    return render(request,'"""+dapp+"""/index.html',{'param1':"hello world"})"""
f1.write(any)
f1.close()

f1=open("urls.py","w")
f1.write("""from django.urls import path
from app1.views import home
urlpatterns = [path('', home),]""")
f1.close()

os.makedirs(f"templates/{dapp}")
os.chdir(f"templates/{dapp}")
f1=open("index.html","w")
f1.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>Hello World</p>
    <p>{{param1}}</p>
</body>
</html>
""")
f1.close()

