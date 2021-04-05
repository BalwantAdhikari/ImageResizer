from django.db import models

class Images(models.Model):
    image_name = models.CharField(max_length=100)
    image_width = models.IntegerField()
    image_height = models.IntegerField()
    image = models.ImageField(upload_to='originalImages')

    def __str__(self):
        return self.image_name


class ResizedImages(models.Model):
    image_name = models.CharField(max_length=100)
    image_width = models.IntegerField()
    image_height = models.IntegerField()
    image = models.ImageField(upload_to='resizedImages')

    def __str__(self):
        return self.image_name