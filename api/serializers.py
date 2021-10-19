from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import Todo


class UserSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')


class TodoReadSerializer(serializers.ModelSerializer):
    """when we are using get method load this class"""
    priority = serializers.CharField(source="get_priority_display")

    class Meta:
        model = Todo

        fields = (
            "id", "title",
            "description", 'priority',
            "last_update_at", "created_at",
        )
        read_only_fields = ("last_update_at", "created_at",)


class TodoWriteSerializer(serializers.ModelSerializer):

    priority = serializers.ChoiceField(
        choices=Todo.PriorityChoices)
    # user = serializers.PrimaryKeyRelatedField(
    #     queryset=get_user_model().objects.all(),
    # )

    class Meta:
        model = Todo

        fields = (
            "id", "title", "user_id",
            "description", 'priority',
        )

    def create(self, validated_data):
        print(self.context["request"].user)
        return Todo.objects.create(**validated_data, user=self.context["request"].user)
