from rest_framework import serializers

from .models import Todo
from .utils.serializers import ValidatorSerializer


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'completed', 'status')


class TodoFilterSerializer(ValidatorSerializer):
    type = serializers.CharField(required=False)
