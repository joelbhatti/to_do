from django.urls import path
from .views import TodoListView
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('todos/', TodoListView.as_view(), name='todo-list'),
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),

]