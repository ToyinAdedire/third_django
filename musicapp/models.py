from datetime import datetime
from turtle import title
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    age = models.IntegerField()
    
    def __str__(self):
        return self.first_name
    
    
class song(models.Model):
    title = models.CharField(max_length = 40)
    date_released = models.DateTimeField(auto_now_add=False)
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(song, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.content
