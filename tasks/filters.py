import django_filters

from .models import Task

class TaskFilter(django_filters.FilterSet):
    priority = django_filters.ChoiceFilter(choices=Task.Priority.choices)
    status = django_filters.ChoiceFilter(choices=Task.Status.choices)
    created_at = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    
    class Meta:
        model = Task
        fields = ['priority', 'status', 'created_at']