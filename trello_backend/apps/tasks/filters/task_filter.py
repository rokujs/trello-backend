import django_filters

from apps.tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Task
        fields = ('name', 'id')
