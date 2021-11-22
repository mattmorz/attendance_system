from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.cache import cache_control
from attendance_app.models import Student

# Create your views here.
def index(request):
    return render(request, 'attendance_app/index.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def loggedIn(request):
    if request.user.is_authenticated:
        user = request.user
        username = user.username
        user_id = user.id
        user_profile = Student.objects.filter(user__id=user_id)
        print (user_profile)
        template = loader.get_template('attendance_app/home.html')
        context = {
            'username': username,
            'user_profile': user_profile
        }
        return HttpResponse(template.render(context,request))
    else:
        return redirect('index')

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
                'error': ''
            }
        return HttpResponse(template.render(context,request))