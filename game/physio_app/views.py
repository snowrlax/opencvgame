from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from physio_app.models import UserProfile, saveEmail

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # Add logic for validating login credentials
        if form.is_valid():
            # Redirect to the 'physio_category' page upon successful login
            return redirect('physio_category')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def email(request):
    uEmail = request.POST.get('email_address')
    uObj = saveEmail(Email = uEmail)
    uObj.save()

    return render(request, 'index.html', {'msg': 'Your Email has been recorded'})

def game_selection(request):
    # Your view logic here
    return render(request, 'game_selection.html')

def physio_category(request):
    return render(request, 'physio_category.html')

def general_well(request):
    return render(request, 'Genral_well_game.html')


def cardiac(request):
    return render(request, 'cardiac_game.html')


def fall_prevention(request):
    return render(request, 'Fall_pre_game.html')


def orthopedic(request):
    return render(request, 'ortho_game.html')