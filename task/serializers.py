from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Task


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'mobile', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('id')

    def create(self, validated_data):
        user = User.objects.get_or_create(**validated_data)
        return user

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)
    assigned_to_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=User.objects.all(),
        source='assigned_to'
    )

    class Meta:
        model = Task
        fields = (
            'id', 'name', 'description', 'task_type', 'status',
            'created_at', 'updated_at', 'completed_at',
            'assigned_to', 'created_by', 'assigned_to_ids'
        )
        read_only_fields = ('id', 'created_at', 'updated_at', 'created_by')
