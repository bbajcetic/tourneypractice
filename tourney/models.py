from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, 
            null=True, 
            on_delete=models.CASCADE)
    wins = models.PositiveIntegerField(default=0)
    def __str__(self):
        return '%s' % (self.user.username)

class Tourney(models.Model):
    name = models.CharField(max_length=30,
            blank=True,null=True)
    winner = models.ForeignKey(Profile, 
            related_name='tourneywinner', 
            blank=True,null = True, 
            on_delete=models.CASCADE)
    size = models.PositiveIntegerField()
    player = models.ManyToManyField(Profile, 
            blank=True,null=True)
    def __str__(self):
        return '%s' % (self.name)

class Match(models.Model):
    winner = models.ForeignKey(Profile, 
            related_name='matchwinner', 
            blank=True,null=True,
            on_delete=models.CASCADE)
    player1 = models.ForeignKey(Profile, 
            blank=True,null=True, 
            related_name='player1', 
            on_delete=models.CASCADE)
    player2 = models.ForeignKey(Profile, 
            blank=True,null=True, 
            related_name='player2', 
            on_delete=models.CASCADE)
    tourney = models.ForeignKey(Tourney, 
            blank=True,null=True,
            on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.id)

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
