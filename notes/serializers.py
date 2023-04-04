from rest_framework import serializers

from notes.models import Note, Tag


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'user', 'text', 'created_at', 'tags']
        read_only_fields = ['user']

    def create(self, validated_data):
        # self.context['request']
        # self.context['view']
        # self.context['format']
        # validated_data["creator"] = self.context["request"].user

        note = super().create(validated_data)
        note.tags.add(Tag.objects.get(id=2))
        return note

    def update(self, instance, validated_data):
        pass
