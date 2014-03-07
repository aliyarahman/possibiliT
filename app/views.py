import urlparse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from app.models import Profile
#from clfapplication.forms import ProfileForm


def login(request):
        username =request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
                if user.is_active:
                        login(request, user)

@login_required
def logout_view(request):
        logout(request)
        return render(request, 'logged_out.html')

@login_required
def index(request):
        return render(request, 'index.html')


def createprofile(request):
        return render(request, 'profile.html')

@login_required
def profile(request):
        return render(request, 'profile.html')
