from django.contrib import admin
from django.contrib.auth.models import User
from app.models import BasicInfo, Identities, LookingFor, MoreAbout, ContactInfo, Settings, Message

admin.site.register(BasicInfo)
admin.site.register(Identities)
admin.site.register(LookingFor)
admin.site.register(MoreAbout)
admin.site.register(ContactInfo)
admin.site.register(Settings)
admin.site.register(Message)
