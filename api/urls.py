from django.urls import path
from api import views

app_name='api'

urlpatterns = [
    path('',views.ButtonView.as_view(),name='all_options'),
    path('get_data',views.getDataList, name='get_data'),
    path('export_to_json',views.exportDataToJson, name='export_to_json'),
    path('post_data/',views.postData, name='post_data'),
    path('delete/<pk>/', views.TaskDeleteAPIView.as_view(), name='delete'),
    path('task/<pk>/', views.TaskSingleView.as_view(), name='task'),
    path('update/<pk>/', views.TaskUpdateAPIView.as_view(), name='update'),
]
