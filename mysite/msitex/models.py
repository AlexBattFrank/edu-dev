# from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class SelfPr(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d", blank=True, verbose_name='photo')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(null=True, default=True)

    def __str__(self):
        return f'{self.title},{self.photo}'

    def get_absolute_url(self):
        return reverse('po3st', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'About my hobby and a bit `bout me'
        verbose_name_plural = 'About my hobby and a bit `bout me'
        ordering = ['-title']

