from rest_framework import viewsets
from exercises.models.muscles import Muscle 
from .serializers import MusclesSerializer

class MusclesAPIView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Muscle.objects.all()
    serializer_class = MusclesSerializer

