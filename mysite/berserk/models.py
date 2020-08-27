from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=100)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_name = models.CharField(max_length=100)