# Generated by Django 5.0.6 on 2024-05-14 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmovi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmovi',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='filmovi',
            name='godina',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='filmovi',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='movie-images'),
        ),
        migrations.AddField(
            model_name='filmovi',
            name='imdb_ocena',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='filmovi',
            name='link_za_gledanje',
            field=models.CharField(default='', max_length=320),
        ),
        migrations.AddField(
            model_name='filmovi',
            name='link_za_preuzimanje',
            field=models.CharField(default='', max_length=320),
        ),
        migrations.AddField(
            model_name='filmovi',
            name='link_za_prevod',
            field=models.CharField(default='', max_length=320),
        ),
        migrations.AddField(
            model_name='filmovi',
            name='originalni_naziv',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='filmovi',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]