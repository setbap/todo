from rest_framework.viewsets import ModelViewSet
from api.models import Todo
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated

from api.serializers import TodoReadSerializer, TodoWriteSerializer


class TodoViewSet(ModelViewSet):

    queryset = Todo.objects.all()
    premission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.all().filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return TodoReadSerializer
        return TodoWriteSerializer
