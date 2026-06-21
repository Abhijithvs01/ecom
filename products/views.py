from django.shortcuts import render
from . models import products
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    featured_product = products.objects.order_by('priority')[:3]
    context = {'product':featured_product}
    print(context)
    return render(request, 'index.html',context)
def list_product(request):
    page = 1
    if request.GET:
        page = request.GET.get('page',1)
    product_list = products.objects.order_by('priority')
    product_paginator = Paginator(product_list,3)
    product_list = product_paginator.get_page(page)
    context = {'products':product_list}
    return render(request, 'shop.html', context)
def deatil_product(request,id):
    product = products.objects.get(id = id)
    context = {'product': product}
    return render(request, 'shop-single.html',context)
def product_search(request):
        query = request.GET.get('q','').strip()
        product_list = products.objects.all()

        if query:
            product_list = product_list.filter(title__icontains=query)
        
        context = {
             'products' : product_list,
             'query' : query
        }
        return render(request,'search.html',context)


