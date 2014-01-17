from django.db import models

# Create your models here.
class Todo(models.Model):
	title = models.CharField(max_length=50)
	desc = models.CharField(max_length=300)
	status = models.CharField(max_length=10)
	create_date = models.DateTimeField('create date')
	modify_date = models.DateTimeField('modify date')

	def __str__(self):
		return self.title