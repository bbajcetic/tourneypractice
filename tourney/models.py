from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wins = models.PositiveIntegerField(default=0)

class Tourney(models.Model):
    name = models.CharField(max_length=30,blank=True)
    winner = models.ForeignKey(Profile, related_name='tourneywinner', blank=True, null = True, on_delete=models.CASCADE)
    size = models.PositiveIntegerField()

class Match(models.Model):
    winner = models.ForeignKey(Profile, related_name='matchwinner', on_delete=models.CASCADE)
    player1 = models.ForeignKey(Profile, related_name='player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Profile, related_name='player2', on_delete=models.CASCADE)
    tourney = models.ForeignKey(Tourney, on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=30,blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
