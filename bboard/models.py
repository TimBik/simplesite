from django.db import models


# Create your models here.

class Bb(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
