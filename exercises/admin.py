from django.contrib import admin
from .models import Exercise, Exercise_Done, Admin_Exercise_Done, Muscle, Exercise_Admin

# Register your models here.

admin.site.register(Muscle)
admin.site.register(Exercise, Exercise_Admin)
admin.site.register(Exercise_Done, Admin_Exercise_Done)