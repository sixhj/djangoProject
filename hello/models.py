from django.contrib import admin
from django.db import models


# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('发布日期')
    question_name = models.CharField('名称', max_length=30, default='')

    class Mate:
        verbose_name = '问题'
        verbose_name_plural = '问题'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
