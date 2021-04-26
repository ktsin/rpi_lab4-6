from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name="Author's full name.")

    def __str__(self):
        return f'{self.name}'

    def __unicode__(self):
        return f'{self.name}'