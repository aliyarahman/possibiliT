from django import forms
from django.forms import CharField, Form, PasswordInput, IntegerField, ChoiceField, ChoiceField, BooleanField, FileField, Textarea, RadioSelect, EmailField
from django.contrib.auth.models import User
from app.models import BasicInfo, Identities, LookingFor, MoreAbout, ContactInfo, Settings, Message

class BasicInfoForm(Form):
	over18 = BooleanField()
	birth_day = ChoiceField()
	birth_month = ChoiceField()
	birth_year = ChoiceField()
	city = CharField()
	state = ChoiceField()
	country = ChoiceField()
	zipcode = IntegerField()


class IdentitiesForm(Form):
	gender = CharField()
	orientation = CharField()
   	outness_gender = ChoiceField(required=True, choices=(('1', 'Everyone'),('2', 'Family/Friends'),('3', 'Just to friends'), ('4', 'Just to family'), ('5','Discreet')))
	outness_orientation = ChoiceField(required=True, choices=(('1', 'Everyone'),('2', 'Family/Friends'),('3', 'Just to friends'), ('4', 'Just to family'), ('5','Discreet')))
	relationship_status = ChoiceField(choices=(('1','Single - monogamous'),('2', 'Single - polyamorous'),('3','Not single - monogamous'),('4', 'Non single - polyamorous')))
	ethnicity = CharField()


class LookingForForm(Form):
	gender = CharField(required=True)
	orientation = CharField(required=True)
	age_lower = IntegerField()
	age_upper = IntegerField()
	near_zip = IntegerField()
	within_miles_of_zip = IntegerField()


class CreateAccountForm(Form):
	username = CharField()
	email = EmailField()
	password = CharField(widget=PasswordInput(), required=True)
	retypepassword = CharField(widget=PasswordInput(), required=True)


class MoreAboutForm(Form):
	interests_personal = CharField()
	interests_dating = CharField()
	about_me = CharField(widget=Textarea())
	from_city = CharField()
	from_state = CharField()
	from_country = CharField()
	height = CharField()
	bodytype = CharField()
	profile_photo = FileField()
	background_image = FileField()


class ContactInfoForm(Form):
	phone = CharField()
	street_address = CharField()
	alternate_email = CharField()	


class SettingsForm(Form):
	show_birthday = BooleanField(required = True)
	show_age = BooleanField(required = True)
        receive_message_notifications = BooleanField(required=True)
        receive_newsletter = BooleanField(required=True) 


class MessageForm(Form):
	recipients = CharField()
	subject = CharField()
	text = CharField(required=True)
