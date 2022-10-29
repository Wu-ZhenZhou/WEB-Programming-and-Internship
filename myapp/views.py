from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random
from myapp.models import student

# Create your views here.
def sayhello(request):
    return HttpResponse('sayhello.......')
    
#def hi(request, username):
#    return HttpResponse('hello '+username)
def hi(request, username):
    now = datetime.now()
    return render(request, 'hello3.html', locals())

def hi2(request, username):
    now = datetime.now()
    return render(request, 'hello4.html', locals())

def test_dict(request):
    dict1 = {'key1': 123, 'key2': 456}
    return render(request, 'hello4.html', locals())

def dice(request):
    no= random.randint(1,6)
    return render(request,"dice.html", locals())

def dice2(request):
    no1= random.randint(1,6)
    no2= random.randint(1,6)
    no3= random.randint(1,6)
    return render(request,"dice2.html", locals())

times = 0
def dice3(request):
    global times
    times = times + 1
    local_times = times
    username = "David"
    dict_no = {"no": random.randint(1,6)}
    return render(request,"dice3.html", locals())

def show(request):
    person1={"name":"Amy","phone":"049-1234567","age":20}
    person2={"name":"Jack","phone":"02-4455666","age":25}
    person3={"name":"Nacy","phone":"04-9876543","age":17}
    persons=[person1,person2,person3]
    
    #TODO 9*9 multiplication table
    row_list = []
    for i in range(1,10):
        col_list = []
        for j in range(1,10):
            col_list.append(f'{j} X {i} = {j*i}')
        row_list.append(col_list)

    return render(request,"show.html",locals())

def filter(request):
    value=4
    list1=[1,2,3]
    pw="芝麻開門"
    
    html="<h1>Hello</h1>"
    value2=False
    return render(request,"filter.html",locals()) 

def listone(request):
    try:
        unit = student.objects.get(cName='吳鎮州') #讀取一筆資料
        print('student.objects.get', type(unit))
    except:
        errormessage = " (讀取錯誤!)"
    return render(request, "listone.html", locals())

def listall(request):
    students = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    print('student.objects.all()', type(students))
    return render(request, "listall.html", locals())

def finaltest(request):
    students = student.objects.all().order_by('cHeight')  #讀取資料表, 依 id 遞增排序
    print('student.objects.all()', type(students))
    return render(request, "listall.html", locals())