from django.db import models

from django.db import models


class Drinks(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
