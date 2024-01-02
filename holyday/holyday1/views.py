from django.shortcuts import render
import csv
def printholiday():
    f1=open("holiday/holiday1/Holidays_2024.csv","r")
    list1=[]
    date1=[]
    day1=[]
    name1=[]
    state1=[]
    info1=csv.reader(f1)
    for line in info1:
        list1.append(line)
        date1.append(line[0])
        day1.append(line[1])
        name1.append(line[2])
        state1.append(line[3].replace("\n",""))
    #print(state1)
    for i,s in enumerate(state1):
        if "KA" in s :
            print(date1[i],name1[i]," is a holiday")
#Program not working for national except
printholiday()
    
def holiday(request):
    
    return render(request,"holiday1/index.html")
