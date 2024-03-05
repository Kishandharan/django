from django.shortcuts import render

def home(request):
    def perm3(word3):
        # word3="EAT"
        list1=[]
        s1=word3
        c1=s1[0]
        c2=s1[1]
        c3=s1[2]
        list1.append(c1+c2+c3)
        list1.append(c1+c3+c2)
        list1.append(c2+c1+c3)
        list1.append(c2+c3+c1)
        list1.append(c3+c1+c2)
        list1.append(c3+c2+c1)
        result=list1
        print(result)
        return result
    output=perm3("CAT")
    return render(request,'permutation1/index.html',{'param1':output})


