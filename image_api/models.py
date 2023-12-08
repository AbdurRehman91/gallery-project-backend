from django.db import models

class Image(models.Model):
    url = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_created=True)

    def __str__(self):
        return self.url