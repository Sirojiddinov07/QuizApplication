from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from  rest_framework.views import APIView
from .serializers import *
from .models import *

app_name = "main"
class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()



class RandomQuestions(APIView):

    def get(self, request, format=None, **kwargs):
        question = Questions.objects.filter(quiz__title=kwargs["topic"]).order_by("?")[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data )



class QuizQuestions(APIView):

    def get(self, request, format=None,  **kwargs):
        question = Questions.objects.filter(quiz__title=kwargs["topic"])
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
