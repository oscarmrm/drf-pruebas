from django.db import models
from django.contrib import admin
from .muscles import Muscle

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

    
class Exercise_Done(models.Model):
    id_exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE) #Clave foránea de el ejercicio
    n_sets = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    repeats = models.IntegerField()
    rest = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField()
