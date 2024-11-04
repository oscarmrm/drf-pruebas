from django.db import models
from django.contrib import admin

# Create your models here.

class Muscle(models.Model):
    name = models.CharField(max_length=200)
    is_big_muscle = models.BooleanField()

    def __str__(self):
        return self.name
    

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    muscles = models.ManyToManyField(Muscle, through='Muscle_Exercise')
    
    def __str__(self):
        return self.name
    
class Muscle_Exercise(models.Model):
    muscles = models.ForeignKey(Muscle, on_delete=models.CASCADE)
    exercises = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    is_high_involved = models.BooleanField()

class Muscle_Exercise_Admin(admin.TabularInline):
    model = Muscle_Exercise
    extra = 1

class Exercise_Admin(admin.ModelAdmin):
    inlines = [Muscle_Exercise_Admin]
    
class Exercise_Done(models.Model):
    id_exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE) #Clave foránea de el ejercicio
    n_sets = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    repeats = models.IntegerField()
    rest = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField()


class Admin_Exercise_Done(admin.ModelAdmin):
    list_display = ('date', 'id_exercise')


"""
Al principio las series van a ser siempre las mismas y van a pertenecer a la clase de ejercicio hecho

class Sets(models.Model):
    id_exercise_done = models.ForeignKey(Exercise_Done, on_delete=models.CASCADE)
    n_set = models.IntegerField()
    are_equal_sets = models.BooleanField()
"""