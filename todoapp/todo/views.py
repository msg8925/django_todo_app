from django.shortcuts import render
from .models import Task
#from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView ,CreateView, UpdateView, DeleteView
from .filters import TodoFilter
# from django.contrib.auth.models import User

# Create your views here.

# def correct_user_check():
#     task = Task.objects.filter(username=)
#     if user == user:
#         return True
    
#     else:
#         return False

# @user_passes_test
# @login_required
# def home(request):

#     # Get all tasks from task table
#     #tasks = Task.objects.filter(author=)
#     tasks = Task.objects.all()

#     # Pass tasks to template
#     context = {
#         "tasks": tasks
#     }

#     return render(request, 'todo/home.html', context)

# UserPassesTestMixin,
class TaskListView(LoginRequiredMixin, ListView):
    queryset = Task.objects.all() 
    #model = Task
    context_object_name = 'tasks'
    #fields = ['name', 'status', 'author']


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TodoFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context


    # def test_func(self):
    #     task = self.get_object()
    #     if self.request.user == task.author:
    #         return True
    #     return False


class TaskDetailView(DetailView):
    model = Task
    fields = ['name', 'status']


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name']

    # I don't understand this
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['name', 'status']

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/'
    fields = ['name', 'status']