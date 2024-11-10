from django.urls import path, include
from . import views
from .api import ExerciseDoneAPIView, MusclesAPIView, ExercisesAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"done", ExerciseDoneAPIView, basename='exercise-done')
router.register(r"muscles", MusclesAPIView, basename='msucles')
router.register(r"exercises", ExercisesAPIView, basename='exercises')

urlpatterns = [
    #path('', views.exercises ),
    path('', include(router.urls))
]