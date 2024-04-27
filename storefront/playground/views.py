from django.shortcuts import render
from django.http import HttpResponse

"""
notes:
使用template需要在settings.py中配置TEMPLATES DIRS
"""

def cal():
    x = 1
    y = 2
    return x + y

def sayHello(request):
    x = cal()
    return render(request, 'hello.html', {'name': 'Mosh'})