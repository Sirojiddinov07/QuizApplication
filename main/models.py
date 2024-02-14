from django.db import models
from  django.utils.translation import  gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Quizzes (models.Model):

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural =_("Quizzes")
        ordering = ["id"]
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, default=_("New Quiz"), verbose_name=_("New Title"))
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Updated(models.Model):
    date_updated = models.DateTimeField(auto_now=True, verbose_name=_("Last Updated"))

    class Meta:
        abstract = True

class Questions (Updated):
    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ["id"]


    SCALE = (
        (0, _("Fundamental")),
        (1, _("Beginner")),
        (2, _("Intermediate")),
        (3, _("Advanced")),
        (4, _("Expert"))
    )

    TYPE = (
        (0, _("Multiple choices")),  # Provide a human-readable name for the choice
    )

    quiz = models.ForeignKey(Quizzes, related_name="questions", on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_("Type of questions"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name=_("Difficulty of questions"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date created"))
    is_active = models.BooleanField(default=False, verbose_name=_("Active status"))


    def __str__(self):
        return self.title



class Answers(Updated):
    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ["id"]


    questions = models.ForeignKey(Questions, related_name="answers", on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer text"))
    is_right = models.BooleanField(default=False)


    def __str__(self):
        return self.answer_text

