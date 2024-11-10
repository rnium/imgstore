from typing import Any, Optional
from django.core.management import BaseCommand
from django.utils import timezone
from django.conf import settings
from imgstore.models import Photo
import os


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        qs = Photo.objects.filter(
            uploaded_at__lte = timezone.now() - settings.IMAGE_EXPIRATION_TIMEOUT
        )
        count = qs.count()
        for photo in qs:
            if os.path.exists(str(photo.image.path)):
                os.remove(photo.image.path)
            photo.delete()
        self.stdout.write(f'{count} expired photos deleted', self.style.WARNING)