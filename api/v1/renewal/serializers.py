from rest_framework_bulk import BulkListSerializer

from common.serializers import DynamicFieldsModelSerializer
from renewal.models import Project


class ProjectSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Project
        list_serializer_class = BulkListSerializer
        fields = '__all__'
