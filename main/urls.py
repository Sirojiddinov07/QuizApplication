from django.urls import path
from .views import *

urlpatterns = [
    path("", Quiz.as_view(), name="quiz"),
    path("r/<str:topic>/", RandomQuestions.as_view(), name="random"),
    path('q/<str:topic>/', QuizQuestions.as_view(), name='questions'),

]