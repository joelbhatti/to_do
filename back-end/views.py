from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoListView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer