# tasks\forms.py
from django import forms
from tasks.models import Task

# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True


class CreateTaskForm(forms.ModelForm):
   
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'images', 'priority']
        # widgets = {

        #     # 'images': MultipleFileInput(),
        #     'images': forms.ClearableFileInput(attrs={'multiple': True})
        # }
        # labels = {
        #     'images': 'You can Select Multiple images', 
        # }