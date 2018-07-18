import rest_framework_filters as filters

from renewal.models import Project


class ProjectFilterSet(filters.FilterSet):
    class Meta:
        model = Project
        fields = '__all__'


