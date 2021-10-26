from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'attendance_app/index.html')

def loggedIn(request):
    username = request.user.username
    template = loader.get_template('attendance_app/home.html')
    context = {
        'username': username
    }
    return HttpResponse(template.render(context,request))

def logout_view(request):
    logout(request)
    return redirect('index')

def signup(request):
    template = loader.get_template('attendance_app/index.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            print ('successfully logged in')
            return redirect('home-page')
        else:
            # Return an 'invalid login' error message.
            context = {
                'error': 'Invalid credentials'
            }
            return HttpResponse(template.render(context,request))
    else:
        context = {
                'error': None
            }
        return HttpResponse(template.render(context,request))