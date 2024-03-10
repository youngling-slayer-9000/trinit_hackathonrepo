from django.shortcuts import render,redirect
from .models import UserLogin
from .forms import TutorRegistrationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'login/home.html')

def result(request):
    if request.method == 'POST':
        user_type = request.POST.get("user_type")
        if user_type:
            print("User type selected:", user_type)
            # You can perform further actions based on the user_type value
            if user_type == 'student':
                return render(request, 'login/student_login.html')
            elif user_type == 'tutor':
                return render(request, 'login/tutor_login.html')
            elif user_type == 'register':
                return HttpResponse('dsihsdg')
            else:
                return HttpResponse("Invalid user type.")
        else:
            return HttpResponse("No user type selected.")
    else:
        return HttpResponse("Method not allowed.")

def webpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Save the username and password to the database
        UserLogin.objects.create(username=username, password=password)
        
        # Redirect to success page or render another page
        return HttpResponse('success')  # Assuming 'success' is the name of the success page URL pattern
    else:
        return render(request, 'login/stduent_login.html')

     
def registration(request):
    return render(request,"login/tutor_register.html")




def tutor_registration(request):
    if request.method == 'POST':
        form = TutorRegistrationForm(request.POST)
        
        if form.is_valid():
            print('valid')
            form.save()
            return HttpResponse('success_url')  # Redirect to a success page or any other URL
        else:
            print(form.errors)
    else:
        form = TutorRegistrationForm()
    return render(request, 'login/tutor_register.html', {'form': form})



