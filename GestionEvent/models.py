from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

from django.db import models
from django.contrib.auth.models import User





# Create your models here.

class Utilisateur(models.Model):
    USERNAME_FIELD = 'nom'
    nom = models.CharField(max_length=50)  
    mot_de_passe = models.CharField(max_length=50)
    mail = models.EmailField(default='example@example.com')



def __str__(self):
        return self.nom



class Event(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_images/')
    date = models.DateField()
    lieu = models.CharField(max_length=200,default=" ")
    description = models.TextField()
    ticket_quantity = models.IntegerField(default=0)



