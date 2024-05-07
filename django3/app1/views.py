from django.shortcuts import render
import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="shashank2005@ssv",
    database="db1"
)

curs=conn.cursor()
# curs.execute("CREATE table airport(timings varchar(10))")

def home(request):
    
    f1=open("airport.txt","r")
    info1=f1.readlines()
    list1=info1[0].split(",")
    # for i in list1:
    #     curs.execute(f"""insert into airport(timings) values("{i}");""")
    #     conn.commit()
    return render(request,'app1/index.html',{'param1':list1})