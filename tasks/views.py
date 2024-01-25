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

    def form_valid(self, form):
        # Get the current user
        user = self.request.user
        # Assign the current user to the user field of the Task instance
        form.instance.user = user
        # Call the parent class's form_valid() method to save the form
        return super().form_valid(form)

