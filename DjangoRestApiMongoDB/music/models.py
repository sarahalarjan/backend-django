from django.db import models


# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=70,)   
    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')       
    artist =  models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist =  models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return self.title





