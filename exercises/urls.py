from django.urls import path, include
from exercises.api.muscles.views import MusclesAPIView
from exercises.api.exercises.views import ExerciseDoneAPIView, ExercisesAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"done", ExerciseDoneAPIView, basename='exercise-done')
router.register(r"muscles", MusclesAPIView, basename='msucles')
router.register(r"exercises", ExercisesAPIView, basename='exercises')

urlpatterns = [
    path('', include(router.urls))
]