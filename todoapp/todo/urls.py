from django.urls import path
from . import views


urlpatterns = [
    #path('', views.home, name='todo-home'),
    path('', views.TaskListView.as_view(template_name='todo/home.html'), name='todo-home'),
    path('task/new/', views.TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
]