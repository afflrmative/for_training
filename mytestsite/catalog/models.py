import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


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

class GameLibrarys(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular game across whole library")
    game_list = models.ForeignKey('Games', on_delete=models.SET_NULL, null=True)
    time_add = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["time_add"]


    def __str__(self):
        return '%s (%s)' % (self.id,self.game_list.game_name)
    
    
    
    @property
    def is_overdue(self):
        if self.time_add and date.today() > self.time_add:
            return True
        return False

     

