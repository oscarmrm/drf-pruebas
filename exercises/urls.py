from django.urls import path, include
from . import views
from .api import ExerciseDoneAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"done", ExerciseDoneAPIView, basename='exercise-done')

urlpatterns = [
    path('', views.exercises ),
    path('', include(router.urls))
]