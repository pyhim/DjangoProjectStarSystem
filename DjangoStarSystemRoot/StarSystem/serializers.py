from rest_framework import serializers
from StarSystem.models import Galaxy, StarSystem, Star, Planet

# Create your serializers here


class GalaxySerializer(serializers.ModelSerializer):
    class Meta:
        model = Galaxy
        fields = '__all__'


class StarSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarSystem
        fields = '__all__'


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = '__all__'


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'

