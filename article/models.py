from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
