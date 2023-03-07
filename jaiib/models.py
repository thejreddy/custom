from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    subcode = models.IntegerField(validators=[RegexValidator(regex='^.{4}$', message='Length has to be 4', code='nomatch')])
    questcode = models.IntegerField(validators=[RegexValidator(regex='^.{5}$', message='Length has to be 5', code='nomatch')])
    quest = models.CharField(max_length=500,null=True)
    option1 = models.CharField(max_length=500,null=True)
    option1_correct = models.BooleanField(default=False)
    option2 = models.CharField(max_length=500,null=True)
    option2_correct = models.BooleanField(default=False)
    option3 = models.CharField(max_length=500,null=True)
    option3_correct = models.BooleanField(default=False)
    option4 = models.CharField(max_length=500,null=True)
    option4_correct = models.BooleanField(default=False)
    explanation = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return f"question: {self.quest}, answer: {self.option1}, correct: {self.option1_correct}"
    objects = models.Manager()
