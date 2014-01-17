from django.core.urlresolvers import reverse
from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from todo import models

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'todo/index.html'
	context_object_name = 'todo_list'

	def get_queryset(self):
		"""Return the last five published polls."""
		return models.Todo.objects.order_by('-create_date')[:5]

def add_todo(request):
	return

def search_todo(request):
	return

def modify_todo(request):
	return