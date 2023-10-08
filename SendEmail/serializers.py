from rest_framework import serializers


class EmailSerializer(serializers.Serializer):
    host = serializers.CharField()
    password = serializers.CharField()
    to = serializers.CharField()
    subject = serializers.CharField()
    content = serializers.CharField()
