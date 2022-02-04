from django.contrib import admin

from .models import Trainee, myuser,Intake

# Register your models here.
admin.site.register(myuser)
admin.site.register(Trainee)
admin.site.register(Intake)