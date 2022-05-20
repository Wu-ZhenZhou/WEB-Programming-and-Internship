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
    return render(request, 'hello3.html', {'username':username, 'now':now, 'random1':'wuruwg'})