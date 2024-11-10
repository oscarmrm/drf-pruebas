from django.contrib import admin
from exercises.models.exercises import Exercise,Exercise_Done,Muscle_Exercise
from exercises.models.muscles import Muscle

# Register your models here.

admin.site.register(Muscle)

class Muscle_Exercise_Admin(admin.TabularInline):
    model = Muscle_Exercise
    extra = 1
class Exercise_Admin(admin.ModelAdmin):
    inlines = [Muscle_Exercise_Admin]
admin.site.register(Exercise, Exercise_Admin)
    

class Admin_Exercise_Done(admin.ModelAdmin):
    list_display = ('date', 'id_exercise')

admin.site.register(Exercise_Done, Admin_Exercise_Done)


