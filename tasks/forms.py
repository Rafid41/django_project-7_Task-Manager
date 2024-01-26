# tasks\forms.py
from django import forms
from tasks.models import Task, Images

# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True


class CreateTaskForm(forms.ModelForm):
   
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']


class TaskListForm(forms.ModelForm):
    class Meta:
        model = Task
        fields= ['title','priority','due_date']


class UpdateTaskForm(forms.ModelForm):
   
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority' , 'is_complete']
        labels = {
            'is_complete': 'Mark as Complete', 
        }


class CreateImageForm(forms.ModelForm):
    class Meta:
        model= Images
        fields=['image']
