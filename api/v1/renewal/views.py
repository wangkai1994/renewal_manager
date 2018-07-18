from rest_framework.decorators import detail_route
from rest_framework_bulk import BulkModelViewSet

from api.v1.renewal.filtersets import ProjectFilterSet
from api.v1.renewal.serializers import ProjectSerializer
from renewal.models import Project


class ProjectViewSet(BulkModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_class = ProjectFilterSet

