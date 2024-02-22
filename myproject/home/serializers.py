from rest_framework import serializers
from .models import Ragister


class RagisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ragister
        fields = "__all__"
