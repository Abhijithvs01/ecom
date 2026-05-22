from django.shortcuts import render
from . models import products
# Create your views here.
def index(request):
    return render(request, 'index.html')
def list_product(request):

    product_list = products.objects.all()
    context = {'products':product_list}
    return render(request, 'shop.html')
def deatil_product(request):
    return render(request, 'shop-single.html' )

