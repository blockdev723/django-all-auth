from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'key': ''
    }

    return render(request, 'home/index.html', context)

def profile_view(request):
    return HttpResponse("Welcome %s <br> <a href='/accounts/logout/'>Logout</a>" % request.user)
