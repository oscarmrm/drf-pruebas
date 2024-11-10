from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from .models import Exercise_Done, Muscle, Exercise
from .serializers import ExerciseDoneSerializer, MusclesSerializer, ExerciseSerializer

class ExerciseDoneAPIView(viewsets.ModelViewSet):
    queryset = Exercise_Done.objects.all()
    serializer_class = ExerciseDoneSerializer

    
class MusclesAPIView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Muscle.objects.all()
    serializer_class = MusclesSerializer


class ExercisesAPIView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
