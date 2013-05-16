from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=20)
    desription = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
    lang = models.ForeignKey(Language)
	
def __unicode__(self):
	return '%s' % (self.name)


class Block(models.Model):
    code = models.CharField(max_length=80)
    task =  models.ForeignKey(Task)

def __unicode__(self):
    return self.code


class Check(models.Model):
    input_value = models.CharField(max_length=40)
    output_value = models.CharField(max_length=40)
    task = models.ForeignKey(Task)
    
def __unicode__(self):
    return self.input_value + ' ' + self.input_value 

class Language(models.Model):
	name  = models.CharField(max_length=40)
	accessId = models.IntegerField()

def __unicode__(self):
    return self.input_value + ' ' + self.input_value 
