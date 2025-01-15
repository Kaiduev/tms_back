from rest_framework import viewsets
from django_filters import rest_framework as dj_filters

from .models import Task
from .serializers import TaskSerializer
from .filters import TaskFilter
from .pagination import TaskPagination
from .utils import cache_response


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer
    filter_backends = [dj_filters.DjangoFilterBackend]
    filterset_class = TaskFilter
    pagination_class = TaskPagination

    @cache_response(timeout=15) # Кэширование запросов на получение списка задач
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
