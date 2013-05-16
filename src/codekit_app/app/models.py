from django.db import models

class Language(models.Model):
	name  = models.CharField(max_length=40)
	accessId = models.IntegerField()
	
	
class Task(models.Model):
    name = models.CharField(max_length=20)
    desription = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
    lang = models.ForeignKey(Language)
	

class Block(models.Model):
    code = models.CharField(max_length=80)
    task =  models.ForeignKey(Task)

class Check(models.Model):
    input_value = models.CharField(max_length=40)
    output_value = models.CharField(max_length=40)
    task = models.ForeignKey(Task)



