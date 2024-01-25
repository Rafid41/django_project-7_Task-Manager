from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from tasks.forms import CreateTaskForm
from tasks.models import Task
from django.views.generic.edit import CreateView




class CreateNewTaskView(CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'tasks/create_tasks.html'  
    success_url = reverse_lazy('tasks:create_task')

