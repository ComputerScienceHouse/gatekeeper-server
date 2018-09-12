from rest_framework.serializers import ModelSerializer
from gatekeeper.access_points.models import AccessPoint


class AccessPointSerializer(ModelSerializer):
    class Meta:
        model = AccessPoint
        fields = ['name', 'location']
