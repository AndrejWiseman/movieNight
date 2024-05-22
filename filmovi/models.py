from django.db import models
from django.urls import reverse

# from taggit.managers import TaggableManager


# Create your models here.
class Filmovi(models.Model):
    naslov = models.CharField(max_length=120)
    originalni_naziv = models.CharField(max_length=120, null=True)
    slug = models.SlugField(default="", null=False)
    godina = models.CharField(max_length=120, null=True, blank=True)
    # tags = TaggableManager()
    imdb_ocena = models.CharField(max_length=120, null=True)
    sadrzaj = models.TextField()
    link_za_preuzimanje = models.CharField(default="", max_length=320)
    link_za_prevod = models.CharField(default="", max_length=320)
    link_za_gledanje = models.CharField(default="", max_length=320)
    image = models.FileField(upload_to='movie-images', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.naslov

    def get_absolute_url(self):
        return reverse('filmovi:film_view', kwargs={'slug': self.slug})
