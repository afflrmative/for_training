from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class Games(models.Model):
    game_name = models.CharField(max_length=255)
    description = models.TextField()
    company_name = models.ForeignKey('Companys', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.game_name
    
    
    def get_absolute_url(self):
        return reverse('game-detail', args=[str(self.id)])
    
    


class Companys(models.Model):
    name = models.CharField(max_length=255)
    short_desc = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('company-detail', args=[str(self.id)])
     
    def __str__(self):
        return self.name

     

