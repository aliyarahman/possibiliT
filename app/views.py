import urlparse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from app.models import BasicInfo, Identities, LookingFor, MoreAbout, ContactInfo, Settings, Message
from app.forms import BasicInfoForm, IdentitiesForm, LookingForForm, CreateAccountForm, MoreAboutForm, ContactInfoForm, SettingsForm, MessageForm


#Login/logout views
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


#Landing page
@login_required
def index(request):
        return render(request, 'index.html')


#Profile creation views
def basic_info(request):
        return render(request, 'basic_info.html')

def identities(request):
        return render(request, 'identities.html')

def looking_for(request):
        return render(request, 'looking_for.html')

def create_account(request):
        return render(request, 'create_account.html')


#Existing user profile views
@login_required
def update_profile(request):
        return render(request, 'update_profile.html')

@login_required
def more_about(request):
        return render(request, 'more_about.html')

@login_required
def contact_info(request):
        return render(request, 'contact_info.html')

@login_required
def settings(request):
        return render(request, 'settings.html')

#Inter-user communication views
@login_required
def send_message(request):
        return render(request, 'send_message.html')

