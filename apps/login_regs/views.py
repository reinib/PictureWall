from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, UserManager
import bcrypt

# Create your views here.
def index(response):
    return render(response, "login_regs/index.html")

def register(request):
     return render(request, "login_regs/register.html")

def login(request):
    return render(request, "login_regs/login.html")

def create_user(request):
    response = User.objects.validateUser(request.POST)
    if 'errors' in response:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/register')
    else:
        request.session['user_id'] = response['user_id']
        print(request.session['user_id'])
    return redirect('/wall')

def login_user(request):
    response = User.objects.loginUser(request.POST)
    if 'errors' in response:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/login')
    else:
        request.session['user_id'] = response['user_id']
        return redirect('/wall')

def logout(request):
    request.session.clear()
    return redirect('/')        
