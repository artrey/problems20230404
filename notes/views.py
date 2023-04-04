from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from notes.models import Note
from notes.serializers import NoteSerializer


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=1)
        # serializer.save(user=self.request.user)
        # serializer.save(user=User.objects.get(id=1))

    def get_permissions(self):
        if self.action == 'favourite':
            return [HasSubscription()]
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated()]
        return []

    @action(detail=False, url_path='fav')
    def favourite(self, request, *args, **kwargs):
        pass
