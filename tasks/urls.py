# tasks\urls.py
from django.urls import path
from tasks import views


app_name = 'tasks'



urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    # path('product/<pk>/', views.ProductDetail.as_view(), name='product_detail'),
    
    path('create_task/',views.CreateNewTaskView.as_view(), name='create_task'),
]