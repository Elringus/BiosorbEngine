from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    allowGame = models.BooleanField(default=False)
    score = models.IntegerField(default=0)

    def __str__(self):
        return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Article(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to="uploads/news", default='/static/images/news_dummy.jpg')
    intro = models.TextField()
    text = models.TextField()

    def unescaped_text(self):
        return mark_safe(self.text)

    def __unicode__(self):
        return self.title
