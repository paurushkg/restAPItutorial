from rest_framework import serializers

from status.models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
            'timestamp'
        ]

    def validate_content(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError('Very Long Text')
        return value

    def validate(self, data):
        content = data.get('content', None)
        if content is None:
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError('Content or Image required!')
        return data
