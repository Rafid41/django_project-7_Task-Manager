from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from tasks.forms import CreateTaskForm, TaskListForm
from tasks.models import Task
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView




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
    

class TaskListView(ListView):
    model = Task
    form_class = TaskListForm
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        
    
         # Search functionality
        search = self.request.GET.get('search', '').strip()
        if search:
            queryset = queryset.filter(title__icontains=search)

        return queryset

