from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculate():
    x = 1
    y = 2
    return x + y

def say_hello(request):
    return render(request, 'hello.html', {"name": [1,2,3]})
