from django.db import models
import datetime

# Create your models here.
from django.utils import timezone


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text

class ProjectInfo(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=32)
    path = models.FilePathField(path="E:/Apache", allow_folders=True, recursive=True)

