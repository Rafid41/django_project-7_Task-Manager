from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from tasks.forms import CreateTaskForm, TaskListForm, UpdateTaskForm, CreateImageForm
from tasks.models import Task, Images
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView




class CreateNewTaskView(CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'tasks/create_tasks.html'  
    success_url = reverse_lazy('tasks:create_task')

    def form_valid(self, form):
        # current user
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



class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/detail_task.html'
    context_object_name = 'Task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        context['images'] = task.image_task.all()  # Fetch all images related to the task
        return context


class TaskUpdateView(UpdateView):
    model = Task
    form_class = UpdateTaskForm
    template_name = 'tasks/update_task.html'
    context_object_name = 'Task'
    success_url = reverse_lazy('tasks:task_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'  
    context_object_name = 'Task'
    success_url = reverse_lazy('tasks:task_list')  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Confirm Deletion'
        return context
    

# add image
def add_image_to_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = CreateImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.task = task
            image.save()
            return redirect('tasks:task_detail', pk=pk)
    else:
        form = CreateImageForm()
    return render(request, 'tasks/add_image_to_task.html', {'form': form, 'task': task})



# image detail

class DeleteImageView(DeleteView):
    model = Images
    template_name = 'tasks/image_confirm_delete.html'  
    context_object_name = 'image'
    # success_url = reverse_lazy('tasks:task_list')  
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Confirm Deletion'
        return context
    
    def get_success_url(self):
        # Access the task's primary key (task.pk) associated with the image
        task_pk = self.object.task.pk
        
        return reverse_lazy('tasks:task_detail', kwargs={'pk': task_pk})
