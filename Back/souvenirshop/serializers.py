from rest_framework import serializers
from .models import Souvenir

class SouvenirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Souvenir
        fields = '__all__'
