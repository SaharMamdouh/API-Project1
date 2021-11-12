from rest_framework import serializers
from pinterest.models import Movie

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'