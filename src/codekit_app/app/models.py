from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=20)
    desription = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
    lang = models.CharField(max_length=20)

class Block(models.Model):
    code = models.CharField(max_length=80)
    task = models.ForeignKey(Task)
