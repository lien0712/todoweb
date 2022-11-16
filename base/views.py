from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .models import Task

# Create your views here.
def index(request):
    return HttpResponse('Hello')

class TaskList(ListView): # find task_list.html if not return 
    model = Task  #listView require a model or queryset
    context_object_name='tasks'
    
class TaskDetail(DetailView): #find task_detail.html
    model=Task
    context_object_name='task'
    template_name='base/task.html'# look for task.html instead of task_detail.html

class TaskCreate(CreateView):
    model= Task
    fields='__all__' # list all item of fields
    success_url=reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model=Task
    fields='__all__' 
    success_url=reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model=Task
    context_object_name='task'
    success_url=reverse_lazy('tasks')
