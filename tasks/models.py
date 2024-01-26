from django.db import models
from django.contrib.auth.models import User

# Create your models here.


    


class Task(models.Model):

    LOW = 1
    MEDIUM = 2
    HIGH = 3
    
    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_user')
    title = models.CharField(max_length=264,  blank= False)
    description = models.TextField(blank=True)
    due_date = models.DateField(blank=False)
    #images = models.ImageField(upload_to='photos/')
    # images = models.ManyToManyField(Image, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
  
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['-priority', 'due_date']

    def __str__(self):
        return str(self.title)
    


class Images(models.Model):
    task =  models.ForeignKey(Task, on_delete=models.CASCADE, related_name='image_task')
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return str(self.image) 
 