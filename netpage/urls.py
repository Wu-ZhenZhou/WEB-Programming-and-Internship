"""netpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import sayhello
from myapp.views import hi
from myapp.views import hi2
from myapp.views import test_dict
from myapp.views import dice, dice2, dice3, show, listone, listall, finaltest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sayhello),
    path('hi/<str:username>', hi),
    path('hi2/<str:username>', hi2),
    path('test-dict/', test_dict),
    path('dice/', dice),
    path('dice2/', dice2),
    path('dice3/', dice3),
    path('show/', show),
    path('listone/', listone),
    path('listall/', listall),
    path('finaltest/', finaltest),
]
