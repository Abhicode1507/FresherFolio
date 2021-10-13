from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

#home page
def home_page(request):
    return render(request,'enroll/index.html')

def education_page(request):
    return render(request,'enroll/education.html')

def experience_page(request):
    return render(request,'enroll/experience.html')

def projects_page(request):
    return render(request,'enroll/projects.html')

def contact_page(request):
    return render(request,'enroll/contact.html')

#sign up view function
def sign_up(request):
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully !!! ')
            fm.save()
    else:
        fm=SignUpForm()
    return render(request,'enroll/signup.html',{'form':fm})

#login view function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
        else:
            fm=AuthenticationForm() 
        return render(request,'enroll/userlogin.html',{'form':fm})

    else:
        return HttpResponseRedirect('/profile/')

#profile
def user_profile(request):
    return render(request,'enroll/profile.html',{'name':request.user})

#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')