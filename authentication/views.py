from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ReservationForm
from django.shortcuts import render, redirect
from .models import Reservation



def home(request):
    return render(request, 'authentication/html.html')





def SIGNUP(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('Confirm')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "Username or email already exists.")
            return render(request, "authentication/SIGNUP.html")

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "authentication/SIGNUP.html")

        # Create the user
        user = User.objects.create_user(username, email, password)
        user.save()

        messages.success(request, "Your account has been successfully created.")
        return redirect('signin')

    return render(request, "authentication/SIGNUP.html")




def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            username = user.username
            return render(request, "authentication/html.html", {'username': username})
        else:
            messages.error(request, "Error")
            messages.success(request, "logged in successfully")
            return redirect('signin')

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "logged out successfully")
    return redirect('home')






def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your reservation has been submitted.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'home', context)


def reservation_view(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'authentication/reservation_view.html', context)



