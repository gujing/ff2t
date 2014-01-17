from django.core.urlresolvers import reverse
from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse,HttpResponseRedirect
from task import models

# Create your views here.
def index(request):
	user_list = get_list_or_404(models.Employee)
	return render(request,'task/TaskAdd.html',{'user_list':user_list})

def get_task(request, task_id):
	task = get_object_or_404(models.Task,pk=task_id)
	return render(request,'task/TaskDetail.html',{'task':task})

def get_all_task(request):
	task_list = models.Task.objects.all()
	data_context = {'task_list':task_list}
	return render(request,'task/TaskList.html',data_context)

def add_task(request):
	user = get_object_or_404(models.Employee,pk=request.POST['emp_id'])
	task = models.Task()
	task.owner = user
	task.desc = request.POST['desc']
	task.up_task_id = -1
	task.save()
	return HttpResponseRedirect(reverse('tasks:detail', args=(task.id,)))

# Todo Views place here
def add_todo(request):
	return

def search_todo(request):
	return

def modify_todo(request):
	return