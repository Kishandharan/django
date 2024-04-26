import os
dproject=input("Enter the django project name: ")
dapp=input("Enter the django app name: ")
try:
    assert f'{dapp}' in os.listdir(f'{dproject}') and f'{dproject}' in os.listdir('./')
    os.chdir(dproject)
    os.chdir(f"./{dproject}")
    f1=open("settings.py","r+")
    info1=f1.read()
    if f"{dapp}'," not in info1:
        a=info1.replace("'django.contrib.staticfiles',",f"'django.contrib.staticfiles',\n\t'{dapp}',")
        f1.seek(0)
        f1.write(a)
    f1.close()

    f1=open("urls.py","r+")
    info1=f1.read()
    if f"{dapp}.urls" not in info1 and "from django.urls import path,include" not in info1:
        any1=info1.replace("path('admin/', admin.site.urls),",f"""path('admin/', admin.site.urls),\n\tpath("{dapp}/" ,include("{dapp}.urls")),""").replace("from django.urls import path","from django.urls import path,include")
        f1.seek(0)
        f1.write(any1)
    elif f"""path('admin/', admin.site.urls),\n\tpath("{dapp}/" ,include("{dapp}.urls")),""" not in info1:
        any1=info1.replace("path('admin/', admin.site.urls),",f"""path('admin/', admin.site.urls),\n\tpath("{dapp}/" ,include("{dapp}.urls")),""")
        f1.seek(0)
        f1.write(any1)
    f1.close()

    os.chdir(f"../{dapp}")

    f1=open("views.py","w")
    any="""from django.shortcuts import render
from """+dapp+""".forms import inputform
def home(request):
    result = None
    n1 = None
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("name")
            n2=data.get("age")
            return render(request,\""""+dapp+"""/index.html",{'param1':n1, 'param2':n2, 'form':form1})
    else:
        form1=inputform()  
    return render(request,\""""+dapp+"""/index.html",{'form':form1})
"""
    f1.write(any)
    f1.close()

    if os.path.exists('forms.py')==False:
        open('forms.py','w')
    f1=open('forms.py','w')
    f1.write("""from django import forms
class inputform(forms.Form):
    name=forms.CharField(max_length=10,label="name")
    age=forms.IntegerField(min_value=1,max_value=200,label="age")""")
    f1.close()

    if os.path.exists('urls.py')==False:
        open('urls.py','w')
    f1=open("urls.py","r+")
    if "urlpatterns = [" not in f1.read():
        f1.write(f"from django.urls import path\nfrom {dapp}.views import home\nurlpatterns = [\n\tpath('', home),]")
    else:
        a=f1.read().replace("urlpatterns = [",f"urlpatterns = [\n\tpath('', home),").replace("from django.urls import path",f"from django.urls import path\nfrom {dapp}.views import home")
        f1.seek(0)
        f1.write(a)
    f1.close()

    if os.path.exists(f"templates/{dapp}")==False:
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
    <h1>Factorial Program</h1>
    <form method="POST">
    {% csrf_token %}
    {{form.as_p}}    
    <button type="submit">submit</button>
    </form>
    {% if param1 %}
    <h1>{{param1}}</h1>
    <h3>{{param2}}</h3>
    {% endif %}
</body>
</html>""")
    f1.close()
except AssertionError:
    list1 = os.listdir(f'{dproject}')
    list1.remove('db.sqlite3')
    list1.remove('manage.py')
    list1.remove(f'{dproject}')
    print(f'You have {list1} apps in your project')
    print("App not created or check wether the app is created inside the project")
    print(f"run command 'django-admin startapp {dapp}'")

except FileNotFoundError:
        print(f"project name '{dproject}' not found")
