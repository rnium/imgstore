from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/', max_length=1000)
    uploaded_at = models.DateTimeField(auto_now_add=True)