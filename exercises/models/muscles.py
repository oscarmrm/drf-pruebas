from django.db import models

class Muscle(models.Model):
    name = models.CharField(max_length=200)
    is_big_muscle = models.BooleanField()

    def __str__(self):
        return self.name
    