from rest_framework import serializers
from autos_api.models import Autos,User

class AutosSerealizer (serializers.ModelSerializer):
    class Meta:
        model = Autos
        fields = '__all__'

class UserSerealizar (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'