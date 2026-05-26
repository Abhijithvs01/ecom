from django.shortcuts import render
from . models import products
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render(request, 'index.html')
def list_product(request):
    page = 1
    if request.GET:
        page = request.GET.get('page',1)
    product_list = products.objects.all()
    product_paginator = Paginator(product_list,1)
    product_list = product_paginator.get_page(page)
    context = {'products':product_list}
    return render(request, 'shop.html', context)
def deatil_product(request):
    return render(request, 'shop-single.html' )

