from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=25, blank='')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
