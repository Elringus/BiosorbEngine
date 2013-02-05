from django.db import models
from django.utils.safestring import mark_safe

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
