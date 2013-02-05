from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Player(models.Model):
    user = models.OneToOneField(User)
    allowGame = models.BooleanField(default=False)
    level = models.IntegerField(default=1)

    def __unicode__(self):
        return self.user.username

def create_player(sender, instance, created, **kwargs):
    if created:
        profile, created = Player.objects.get_or_create(user=instance)

post_save.connect(create_player, sender=User)