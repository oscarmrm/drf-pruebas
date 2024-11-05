from rest_framework import serializers
from .models import Exercise_Done

class ExerciseDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise_Done
        fields = '__all__'
    