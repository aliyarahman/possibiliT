from django import forms
from django.forms import CharField, Form, PasswordInput, IntegerField, ChoiceField, ChoiceField, BooleanField, FileField, Textarea, RadioSelect, EmailField
from django.contrib.auth.models import User
from app.models import BasicInfo, Identities, LookingFor, MoreAbout, ContactInfo, Settings, Message

class BasicInfoForm(Form):
	over18 = ChoiceField(widget=RadioSelect, choices=((True,'Yes'),(False,'No')))
	birth_month = ChoiceField(choices=((1,'January'),(2,'February'),(3,'March'),(4,'April'),(5,'May'),(6,'June'),(7,'July'),(8,'August'),(9,'September'),(10,'October'),(11,'November'),(12,'December')))
	birth_day = ChoiceField(choices=((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'),(11,'11'),(12,'12'),(13,'13'),(14,'14'),(15,'15'),(16,'16'),(17,'17'),(18,'18'),(19,'19'),(20,'20'),(21,'21'),(22,'22'),(23,'23'),(24,'24'),(25,'25'),(26,'26'),(27,'27'),(28,'28'),(29,'29'),(30,'30'),(31,'31')))
	birth_year = IntegerField()
	city = CharField()
	state = ChoiceField(choices=(('AL','AL'),('AK','AK'),('AZ','AZ'),('AR','AR'),('CA','CA'),('CO','CO'),('CT','CT'),('DC','DC'),('DE','DE'),('FL','FL'),('GA','GA'),('HI','HI'),('ID','ID'),('IL','IL'),('IN','IN'),('IA','IA'),(17,'KS'),('KY','KY'),('LA','LA'),('ME','ME'),('MD','MD'),('MA','MA'),('MI','MI'),('MN','MN'),('MS','MS'),('MO','MO'),('MT','MT'),('NE','NE'),('NV','NV'),('NH','NH'),('NJ','NJ'),('NM','NM'),('NY','NY'),('NC','NC'),('ND','ND'),('OH','OH'),('OK','OK'),('OR','OR'),('PA','PA'),('RI','RI'),('SC','SC'),('SD','SD'),('TN','TN'),('TX','TX'),('UT','UT'),('VT','VT'),('VA','VA'),('WA','WA'),('WV','WV'),('WI','WI'),('WY','WY'),('NONE','Other')))
	country = CharField()
	zipcode = IntegerField()


class IdentitiesForm(Form):
	gender = CharField()
	orientation = CharField()
   	outness_gender = ChoiceField(required=True, choices=(('1', 'To everyone'),('2', 'To family/friends'),('3', 'Just to friends'), ('4', 'Just to family'), ('5','Discreet')))
	outness_orientation = ChoiceField(required=True, choices=(('1', 'To everyone'),('2', 'To family/friends'),('3', 'Just to friends'), ('4', 'Just to family'), ('5','Discreet')))
	relationship_status = ChoiceField(choices=(('1','Single and monogamous'),('2', 'Single and not monogamous'),('3','Not single and monogamous'),('4', 'Not single and not monogamous')))
	ethnicity = CharField()


class LookingForForm(Form):
	lookingfor_gender = CharField(required=True)
	lookingfor_orientation = CharField(required=True)
	age_lower = IntegerField()
	age_upper = IntegerField()
	near_zip = IntegerField()
	within_range_of_zip = IntegerField()


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
	from_state = ChoiceField(choices=((' ',' '),('AL','AL'),('AK','AK'),('AZ','AZ'),('AR','AR'),('CA','CA'),('CO','CO'),('CT','CT'),('DC','DC'),('DE','DE'),('FL','FL'),('GA','GA'),('HI','HI'),('ID','ID'),('IL','IL'),('IN','IN'),('IA','IA'),(17,'KS'),('KY','KY'),('LA','LA'),('ME','ME'),('MD','MD'),('MA','MA'),('MI','MI'),('MN','MN'),('MS','MS'),('MO','MO'),('MT','MT'),('NE','NE'),('NV','NV'),('NH','NH'),('NJ','NJ'),('NM','NM'),('NY','NY'),('NC','NC'),('ND','ND'),('OH','OH'),('OK','OK'),('OR','OR'),('PA','PA'),('RI','RI'),('SC','SC'),('SD','SD'),('TN','TN'),('TX','TX'),('UT','UT'),('VT','VT'),('VA','VA'),('WA','WA'),('WV','WV'),('WI','WI'),('WY','WY'),('NONE','Other')))
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
