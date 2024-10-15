from django.http import HttpResponse
from django.shortcuts import render
import datetime

def test(request):
    date=datetime.datetime.now()
    print("test function is called from view")
    return HttpResponse("<h1>Hello this is index page </h1> "+str(date))

def home(request):
    date=datetime.datetime.now()
    isActive=True

    if request.method=='POST':
        check=request.POST.get("check")
        print(check)
        if check is None:isActive=False
        else: isActive=True

    name="Mahi"
    list_of_programs=[
        'check even odd',
        'check prime',
    ]
    student={
       'student_name':"abcd",
       'student_college':"xyz",
    }
    data={
        'date':date,
        'name':name,
        'isActive':isActive,
        'list':list_of_programs,
        'student_data':student

    }
    return render(request,"home.html",data)

def about(request):
    return render(request,"about.html",{})

def services(request):
    return render(request,"services.html",{})