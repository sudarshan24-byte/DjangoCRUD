from django.db import models

# Create your models here.
class Player(models.Model):
    pName = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    # player_id = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    pType = models.CharField(max_length=50)
    bType = models.CharField(max_length=50)