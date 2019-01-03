from rest_framework.serializers import ModelSerializer
from gatekeeper.realms.models import Realm


class RealmSerializer(ModelSerializer):
    class Meta:
        model = Realm
        fields = [
            'name',
            'slot',
            'read_key',
            'auth_key',
            'update_key',
            'public_key',
            'private_key'
        ]
