from django.db import models

# Create your models here.
from django.db import models

class Memes(models.Model):

    # name = models.CharField(max_length=255)
    # message = models.CharField(max_length=255)
    image = models.FileField(upload_to=' ', blank=True)
    title = models.CharField(max_length=255)