from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_admin = models.IntegerField()
    
class Album(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    description = models.TextField()
    bg_color = models.CharField(max_length=20)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.CharField(max_length=255, null=True, blank=True)  
    def __str__(self):
        return self.name        
    
class Song(models.Model):
    name = models.CharField(max_length=100)
    file = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    desc = models.TextField()
    duration = models.CharField(max_length=20)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

class FavoriteSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)   
      

# Create your models here.
