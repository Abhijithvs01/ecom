from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import customer


def sign_out(request):
     logout(request)
     return redirect('/')
def login_page(request):
        if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')

                print("username:",username)
                print("password:",password)

                user = authenticate(
                    request,
                    username=username,
                    password=password
                )

                if user:
                    login(request, user)
                    return redirect('/')

                messages.error(
                    request,
                    "Invalid username or password."
                )

        return render(request, 'login.html')


def register(request):

    if request.method == "POST":

        username = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address = request.POST.get('address')
        phonenumber = request.POST.get('phonenumber')

        # Password validation
        if password != confirm_password:
            messages.error(
                request,
                "Passwords do not match."
            )
            return render(request, 'register.html')

        # Username already exists
        if User.objects.filter(username=username).exists():
            messages.error(
                request,
                "This username is already taken."
            )
            return render(request, 'register.html')

        # Email already exists
        if User.objects.filter(email=email).exists():
            messages.error(
                request,
                "An account with this email address already exists."
            )
            return render(request, 'register.html')

        # Phone validation
        if len(phonenumber) != 10 or not phonenumber.isdigit():
            messages.error(
                request,
                "Please enter a valid 10-digit phone number."
            )
            return render(request, 'register.html')

        # Create User
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Create Customer Profile
        customer.objects.create(
            username=username,
            user=user,
            phone=phonenumber,
            address=address
        )

        # Auto Login
        login(request, user)

        messages.success(
            request,
            "Account created successfully."
        )

        return redirect('/')

    return render(request, 'register.html')
