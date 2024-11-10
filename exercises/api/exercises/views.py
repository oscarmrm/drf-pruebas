from rest_framework import viewsets
from exercises.models.exercises import Exercise,Exercise_Done
from .serializers import ExerciseDoneSerializer, ExerciseSerializer

class ExerciseDoneAPIView(viewsets.ModelViewSet):
    queryset = Exercise_Done.objects.all()
    serializer_class = ExerciseDoneSerializer

class ExercisesAPIView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
