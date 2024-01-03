from django.shortcuts import render
import csv
from holiday.settings import BASE_DIR
import os
from holiday1.forms import inputform
def getholiday():
    f1=open(os.path.join(BASE_DIR,"holiday1/Holidays_2024.csv"),"r")
    list1=[]
    date1=[]
    day1=[]
    name1=[]
    state1=[]
    holidays=[]
    info1=csv.reader(f1)
    for line in info1:
        list1.append(line)
        date1.append(line[0])
        day1.append(line[1])
        name1.append(line[2])
        state1.append(line[3].replace("\n",""))
    
    for i,s in enumerate(state1):
        if "KA" in s :
            holidays.append([date1[i],day1[i],name1[i]])
    return holidays

def holiday(request):
    if request.method=="POST":
        form=inputform(request.POST)
    list1=getholiday()
    print(list1)
    return render(request,"holiday1/index.html",{"param1":list1})
