from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    firstname2 = models.CharField(max_length=45)
    lastname2 = models.CharField(max_length=45)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=90)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    zipcode = models.CharField(max_length=10)


    def __repr__(self):
        return '<User %r>' % (self.email)

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def __unicode__(self):
        return self.email

    def get_id(self):
        return self.id
