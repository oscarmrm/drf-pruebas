from django.db import models
from .exercises import Exercise

class Routine(models.Model):
    name = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=100)
    estimated_duration = models.DurationField()
    description = models.TextField()
    exercises = models.ManyToManyField(Exercise, through='routine_exercises')

    def __str__(self):
        return self.name

class Routine_exercises(models.Model):
    exercises = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    order = models.IntegerField(auto_created=True, editable=True)
    n_sets = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    repeats = models.IntegerField()
    rest = models.DecimalField(max_digits=5, decimal_places=2)