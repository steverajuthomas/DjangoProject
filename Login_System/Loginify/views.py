from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserDetails
from .forms import SignupForm, LoginForm 
from django.http import JsonResponse
from .serializers import UserDetailsSerializer
import json
from django.views.decorators.csrf import csrf_exempt



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

# Implement CRUD Operations -
# Create four additional views functions for CRUD operations.
# Get a single user using by email view: Retrieves and displays
# details of a specific user based on their name .
# Update User details
# To delete a user using its email.


 #Get all user details view: Retrieves and displays details of all users.
@csrf_exempt
def all_user_details(request):
    # Fetch data from database and return it as a JSON response
    if request.method == 'GET':
        try:
            users = UserDetails.objects.all() #queryset
            serializer_data=UserDetailsSerializer(users,many=True)
            return JsonResponse(serializer_data.data,safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
@csrf_exempt       
def single_user_details(request,name):
    if request.method == 'GET':
        try:
            user = UserDetails.objects.get(Username=name)
            serializer_data=UserDetailsSerializer(user)
            return JsonResponse(serializer_data.data)
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
@csrf_exempt
def Update_User_Details(request,name):
    if request.method=='PATCH':
            try: 
                user = UserDetails.objects.get(Username=name) 
                input_data=json.loads(request.body)
                serializer_data=UserDetailsSerializer(user,data=input_data,partial=True)
                if serializer_data.is_valid():
                    serializer_data.save()
                    return JsonResponse({
                        'Message': 'User updated successfully'
                    },status=200)
            except user.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
            
@csrf_exempt
def Delete_User_Details_by_email(request,email):
    if request.method == 'DELETE':
            try:
                user = UserDetails.objects.get(Email=email)
                user.delete()
                return JsonResponse({
                    'Message': 'User deleted successfully'
                },status=204)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)