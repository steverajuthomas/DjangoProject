from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserDetails
from .forms import SignupForm, LoginForm 
from django.http import JsonResponse


# Create your views here.
def test_view(request):
    return HttpResponse("Hello, World!")

#Implement views in views.py for signup, login.
def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']
            try:
                user = UserDetails.objects.get(Email=email)
                if user.Password == password: 
                    return HttpResponse("Login successful!")  
                else:
                    return render(request, 'Loginify/loginpage.html', {'form': form, 'error': 'Invalid password.'})
            except UserDetails.DoesNotExist:
                return render(request, 'Loginify/loginpage.html', {'form': form, 'error': 'Invalid username and password.'})
        else:
            return render(request, 'Loginify/loginpage.html', {'form': form, 'error': JsonResponse({'error': form.errors})})
    else:
        form = LoginForm()

    return render(request, 'Loginify/loginpage.html', {'form': form})

def signup_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            if UserDetails.objects.filter(Email=email).exists():
                form.add_error('Email', 'A user with this email already exists.')
            else:
                form.save()
                return redirect('login-page') 
    else:
        form = SignupForm()

    return render(request, 'Loginify/signup.html', {'form': form})
