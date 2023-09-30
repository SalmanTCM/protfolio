from django.db import models

class Hero(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='hero_images/')

    def __str__(self):
        return self.title
