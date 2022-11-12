import django_filters
from .models import Task

class TodoFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            'name': ['icontains'], 
            #'author': ['exact'] 
        }

