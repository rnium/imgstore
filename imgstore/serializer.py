from rest_framework import serializers
from django.conf import settings
from .models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image', 'uploaded_at']
    
    def validate_image(self, value):
        image_max_size = settings.MAX_IMGSIZE_MB * 1024 * 1024
        if value.size > image_max_size:
            raise serializers.ValidationError(f'Image size limit {settings.MAX_IMGSIZE_MB}MB exceeds')
        return value
