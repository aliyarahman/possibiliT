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
def login_view(request):
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
        return render(request, 'index.html', {'user':request.user})


#Profile creation views
def basic_info(request):
	if request.method == 'POST':
		form = BasicInfoForm(request.POST)
		if form.is_valid():
			request.session['over18'] = request.POST['over18']
			request.session['birth_month']=request.POST['birth_month']
			request.session['birth_day']=request.POST['birth_day']
			request.session['birth_year']=request.POST['birth_year']
			request.session['city']=request.POST['city']
			request.session['state']=request.POST['state']
			request.session['country']=request.POST['country']
			request.session['zipcode']=request.POST['zipcode']
			return HttpResponseRedirect('../identities')
	else:
		form = BasicInfoForm()
	return render(request, 'basic_info.html', {'form': form})

def identities(request):
	if request.method == 'POST':
		form = IdentitiesForm(request.POST)
		if form.is_valid():
			request.session['gender'] = request.POST['gender']
			request.session['orientation']=request.POST['orientation']
			request.session['outness_gender']=request.POST['outness_gender']
			request.session['outness_orientation']=request.POST['outness_orientation']
			request.session['relationship_status']=request.POST['relationship_status']
			request.session['ethnicity']=request.POST['ethnicity']			
			return HttpResponseRedirect('../looking_for')
	else:
		form = IdentitiesForm()
	return render(request, 'identities.html', {'form': form})

def looking_for(request):
	if request.method == 'POST':
		form = LookingForForm(request.POST)
		if form.is_valid():
			request.session['lookingfor_gender'] = request.POST['lookingfor_gender']
			request.session['lookingfor_orientation']=request.POST['lookingfor_orientation']
			request.session['age_lower']=request.POST['age_lower']
			request.session['age_upper']=request.POST['age_upper']
			request.session['within_range_of_zip']=request.POST['within_range_of_zip']
			request.session['near_zip']=request.POST['near_zip']	
			return HttpResponseRedirect('../create_account')
	else:
		form = LookingForForm()
	return render(request, 'looking_for.html', {'form': form})

def create_account(request):
	if request.method == 'POST':
		form = CreateAccountForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(username = request.POST['username'], password = request.POST['password'], email = request.POST['email'])
			new_user.save()
			username = request.POST['username']
			password = request.POST['email']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
			new_basicinfo = BasicInfo(user = new_user, over18 = request.session['over18'], birth_month=request.session['birth_month'], birth_day=request.session['birth_day'], birth_year=request.session['birth_year'], city=request.session['city'], state=request.session['state'], country=request.session['country'], zipcode=request.session['zipcode'])
			if request.session['birth_day'] <10:
				birth_day = "0"+str(request.session['birth_day'])
			else:
				birth_day = str(request.session['birth_day'])
			if request.session['birth_month'] <10:
				birth_month = "0"+str(request.session['birth_month'])
			else:
				birth_month = str(request.session['birth_month'])
			birth_year = str(request.session['birth_year'])
			new_basicinfo.birth_date_full = birth_year+"-"+birth_month+"-"+birth_day+" 00:00:00"
			new_basicinfo.save()
			new_identities = Identities(user= new_user, gender=request.session['gender'], orientation=request.session['orientation'], outness_gender=request.session['outness_gender'], outness_orientation=request.session['outness_orientation'], relationship_status=request.session['relationship_status'], ethnicity=request.session['ethnicity'])
			new_identities.save()
			new_lookingfor=LookingFor(user = new_user, lookingfor_gender=request.session['lookingfor_gender'], lookingfor_orientation=request.session['lookingfor_orientation'], age_lower=request.session['age_lower'], age_upper=request.session['age_upper'], within_range_of_zip=request.session['within_range_of_zip'], near_zip=request.session['near_zip'])
			new_lookingfor.save()
			return HttpResponseRedirect('../index')
	else:
		form = CreateAccountForm()
	return render(request, 'create_account.html', {'form': form})


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

