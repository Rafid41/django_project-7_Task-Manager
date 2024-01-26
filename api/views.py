from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import DestroyAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework import status
from tasks.models import Task, Images
from api.serializers import TaskSerializer, UserSerializer, ImagesSerializer
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
import json

@api_view(['GET'])
def getDataList(request):
    # tasks = Task.objects.all()
    tasks = Task.objects.filter(user=request.user)
    serializer = TaskSerializer(tasks, many=True) # 1 item fetch korle false hbe
    return Response(serializer.data)



@api_view(['GET'])
def exportDataToJson(request):
   
    ############ Task ###################
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    serialized_data = serializer.data
    
    file_path = 'database_table_Task.json'
    
    with open(file_path, 'w') as file:
        json.dump(serialized_data, file)

    ########### User ###############
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    serialized_data = serializer.data
    
    file_path = 'database_table_User.json'
    
    with open(file_path, 'w') as file:
        json.dump(serialized_data, file)

    ########### Images ###############
    images = Images.objects.all()
    serializer = ImagesSerializer(images, many=True)
    serialized_data = serializer.data
    
    file_path = 'database_table_Images.json'
    
    with open(file_path, 'w') as file:
        json.dump(serialized_data, file)
    
    return Response({'message': 'Data exported to JSON file'}, status=status.HTTP_200_OK)







@api_view(['POST'])
def postData(request):
    serializer = TaskSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




class ButtonView(View):
    template_name = 'api/api_buttons.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    




class TaskDeleteAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    

# single data entry
class TaskSingleView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# update
class TaskUpdateAPIView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer