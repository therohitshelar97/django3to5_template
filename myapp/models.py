from django.db import models

# Create your models here.
class form_table(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
