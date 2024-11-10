from rest_framework import serializers
from .models import Exercise_Done, Muscle, Muscle_Exercise, Exercise

class ExerciseDoneSerializer(serializers.ModelSerializer):
    exercise_name = serializers.SerializerMethodField()

    class Meta:
        model = Exercise_Done
        fields = '__all__'

    def get_exercise_name(self, obj): 
        return obj.id_exercise.name
    

class MusclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    involved_muscles = serializers.SerializerMethodField()
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'involved_muscles']

    def get_involved_muscles(self, obj): 
        muscle_exercises = Muscle_Exercise.objects.filter(exercises=obj)
        return MuscleExerciseSerializer(muscle_exercises, many = True).data
    

class MuscleExerciseSerializer(serializers.ModelSerializer):
    muscle_name = serializers.CharField(source='muscles.name')  # Accede al campo 'name' de la FK 'muscles'

    class Meta:
        model = Muscle_Exercise
        fields = ['muscle_name', 'is_high_involved']