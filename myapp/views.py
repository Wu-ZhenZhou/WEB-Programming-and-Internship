from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
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