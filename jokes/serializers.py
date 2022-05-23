from rest_framework import serializers
from .models import DryJoke


class DryJokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DryJoke
        fields = ['id', 'joke', 'author']
