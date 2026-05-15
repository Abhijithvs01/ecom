from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'index.html')
def list_product(request):
    return render(request, 'shop.html')
def deatil_product(request):
    return render(request, 'shop-single.html' )

