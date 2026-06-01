from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from . models import customer

# Create your views here.

def login_page(request):
    if request.POST and 'login' in request.POST:
        email = request.POST.get('email') 
        password = request.POST.get('password')
    return render(request, 'login.html')
def register(request):
    if request.POST and 'register' in request.POST:
        try:
            username = request.POST.get('fullname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            address = request.POST.get('address')
            phonenumber = request.POST.get('phonenumber')

            #create an user account
            user = User.objects.create(
                username = username,
                email = email,
                password = password
            )

            customers = customer.objects.create(
                user = user,
                phone = phonenumber,
                address = address
            )
            return redirect('/')
        except Exception as e:
            error_message = "Duplicate username or invalid credentials"
            messages.error(request,error_message,'error_message')

    return render(request,'register.html')