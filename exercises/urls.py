from django.urls import path, include
from exercises.api.muscles.views import MusclesAPIView
from exercises.api.exercises.views import ExerciseDoneAPIView, ExercisesAPIView
from exercises.api.routines.views import RoutinesAPIView
from rest_framework import routers

router = routers.DefaultRouter()

# Muscles
router.register(r"muscles", MusclesAPIView, basename='msucles')

#Exercises
router.register(r"exercises/done", ExerciseDoneAPIView, basename='exercise-done')
router.register(r"exercises", ExercisesAPIView, basename='exercises')

#Routines
router.register(r"routines", RoutinesAPIView, basename='routines')

urlpatterns = [
    path('', include(router.urls))
] 