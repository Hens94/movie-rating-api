# Generated by Django 4.0.1 on 2022-01-12 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_api', '0002_alter_movie_poster_url'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('movie', 'user')},
        ),
    ]
