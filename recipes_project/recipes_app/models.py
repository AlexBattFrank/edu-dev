from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='recipes', on_delete=models.CASCADE)
