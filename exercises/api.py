from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from .models import Exercise_Done
from .serializers import ExerciseDoneSerializer

class ExerciseDoneAPIView(viewsets.ModelViewSet):
    queryset = Exercise_Done.objects.all()
    serializer_class = ExerciseDoneSerializer
