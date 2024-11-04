from .models import Exercise
from django.http import JsonResponse

# Create your views here.


def exercises(request): 
    exercises = list(Exercise.objects.values())
    print(exercises)
    return JsonResponse(exercises, safe = False)
