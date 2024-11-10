from rest_framework import serializers
from exercises.models.muscles import Muscle

class MusclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = '__all__'

    