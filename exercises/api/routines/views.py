from rest_framework import viewsets
from exercises.models.routines import Routine
from .serializers import RoutineSerializer

class RoutinesAPIView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    ordering_fields = ['order']
    ordering = ['order']
