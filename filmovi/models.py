from django.db import models


# Create your models here.
class Filmovi(models.Model):

    naslov = models.CharField(max_length=120)
    sadrzaj = models.TextField()

    def __str__(self):
        return self.naslov
