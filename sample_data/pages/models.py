from django.db import models

# Create your models here.
class Bio(models.Model):
    profession = models.CharField(max_length=100)
    description = models.TextField() # No maximum character limit
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to="pages_images/", blank=True)