from django.contrib import admin
from physio_app.models import UserProfile, saveEmail

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(saveEmail)