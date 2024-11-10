from rest_framework import serializers
from exercises.models.routines import Routine, Routine_exercises

class RoutineSerializer(serializers.ModelSerializer):
    exercises = serializers.SerializerMethodField()

    class Meta:
        model = Routine
        fields = '__all__'

    def get_exercises(self, obj): 
        routine_exercises = Routine_exercises.objects.filter(routine=obj).order_by('order')
        return RoutineExercisesSerializer(routine_exercises, many = True).data
    
class RoutineExercisesSerializer(serializers.ModelSerializer):
    exercises = serializers.CharField(source='exercises.name')

    class Meta: 
        model = Routine_exercises
        fields = ['order', 'exercises', 'n_sets', 'repeats', 'rest', 'weight']