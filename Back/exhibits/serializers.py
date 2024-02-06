from rest_framework import serializers
from .models import Exhibit

class ExibitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Exhibit
        fields='__all__'