from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    timezone = serializers.CharField(max_length=100)
    current = serializers.DictField()
    hourly = serializers.ListField()
    daily = serializers.ListField()
