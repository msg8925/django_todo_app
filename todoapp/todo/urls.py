from django.urls import path
from . import views


urlpatterns = [
    #path('', views.home, name='todo-home'),
    path('', views.TaskListView.as_view(template_name='todo/home.html'), name='todo-home'),
    path('task/new/', views.TaskCreateView.as_view(template_name='todo/task_create.html'), name='task-create'),
]