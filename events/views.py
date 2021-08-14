from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
# Create your views here.


def say_hello(request):
    query_set = Product.objects.filter(store_price__range=(20, 30))   
    return render(request, 'hello.html', {"name": "Dan", 'products': query_set})
