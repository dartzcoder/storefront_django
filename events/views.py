from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Q, F, Value, Func
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from store.models import Customer
from store.models import Order
from store.models import OrderItem
from tags.models import TaggedItem
# Create your views here.

def say_hello(request):
    query_set = Product.objects.all()
    list(query_set)
    
    return render(request, 'hello.html', {"name": "Dan's store", 'result': query_set})
