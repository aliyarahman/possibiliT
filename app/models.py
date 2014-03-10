from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Django has a built-in User model that works well with the out-of-the-box authentication functions, so we are using it/them.
# That model is created via User.objects.create(username, email, password), and can then also hold first_name and last_name.

#Instead of redefining the entire User class to acommodate our variables and then writing security funtions for it (and on and on), we are "extending" the user model with Staff, Evaluator, Recommender, and Applicant models that reference their User base model via a OneToOneField.

#To reference via the extended class, do something like: 
	#newperson = User.objects.get(email ="person@example.com")
	#newprofile = newperson.profile.zipcode


class BasicInfo(models.Model):
	user = models.OneToOneField(User)
	over18 = models.BooleanField()
        birth_day = models.IntegerField()
        birth_month = models.IntegerField()
        birth_year = models.IntegerField()
        birth_date_full = models.DateTimeField()
        city = models.CharField(max_length=45)
        state = models.CharField(max_length=4)
	country = models.CharField(max_length=45)
        zipcode = models.CharField(max_length=10)
	
	def __unicode__(self):
		return self.id

class Identities(models.Model):
	user = models.OneToOneField(User)
        gender = models.TextField()
        orientation = models.TextField()
        outness_gender = models.IntegerField()
        outness_orientation = models.IntegerField()
        relationship_status = models.IntegerField()
        ethnicity = models.CharField(max_length=45)

        def __unicode__(self):
                return self.id


class LookingFor(models.Model):
        user = models.OneToOneField(User)
        lookingfor_gender = models.TextField()
        lookingfor_orientation = models.TextField()
        age_lower = models.IntegerField()
        age_upper = models.IntegerField()
        near_zip = models.IntegerField(5)
        within_range_of_zip = models.IntegerField(3)

        def __unicode__(self):
                return self.id


class MoreAbout(models.Model):
	user = models.OneToOneField(User)
        interests_personal = models.TextField()
	interests_dating = models.TextField()
	about_me = models.TextField()
        from_city = models.CharField(max_length=45)
        from_state = models.CharField(max_length=4)
        from_country = models.CharField(max_length=45)
        height = models.CharField(max_length=45)
        bodytype = models.CharField(max_length=45)
	profile_photo = models.FileField(upload_to='static/app/userphotos/')
	background_image = models.FileField(upload_to='static/app/userphotos/') 


        def __unicode__(self):
                return self.id


class ContactInfo(models.Model):
	user = models.OneToOneField(User)
	phone = models.CharField(max_length=15)
	street_address = models.CharField(max_length=90)
	alternate_email = models.EmailField()

        def __unicode__(self):
                return self.id


class Settings(models.Model):
	user = models.OneToOneField(User)
	show_birthday = models.BooleanField()
	show_age = models.BooleanField()
	receive_interaction_notifications = models.BooleanField(default = True)
	receive_newsletter = models.BooleanField(default = True)

        def __unicode__(self):
                return self.id


class Message(models.Model):
	sender = models.OneToOneField(User)
	recipients = models.CommaSeparatedIntegerField(max_length=400)
	subject = models.CharField(max_length=140)
	text = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

        def __unicode__(self):
                return self.subject
