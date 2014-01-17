from django.db import models

# Create your models here.

class Employee(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	nickname = models.CharField(max_length=50)

	def __str__(self):
		return self.nickname

class Task(models.Model):
	owner = models.ForeignKey(Employee)
	up_task_id = models.IntegerField(max_length=100)
	compile_status = models.BooleanField(default=0)
	desc = models.CharField(max_length=2000)

	def __str__(self):
		return self.desc

class Todo(models.Model):
	title = models.CharField(max_length=50)
	desc = models.CharField(max_length=300)
	status = models.CharField(max_length=10)
	create_date = models.DateTimeField('create date')
	modify_date = models.DateTimeField('modify date')

	def __str__(self):
		return self.title