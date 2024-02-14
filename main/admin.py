from django.contrib import admin
from .models import *

@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]


class AnswerInlineModel(admin.TabularInline):
    model = Answers
    list_display = [
        "answer_text",
        "is_right"
    ]



@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "quiz"
    ]
    list_display = [
        "title",
        "quiz",
        "date_created"
    ]
    inlines = [AnswerInlineModel]



@admin.register(Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title"
    ]
@admin.register(Answers)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        "answer_text",
        "is_right",
        "questions"
    ]