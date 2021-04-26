from django.db import models


class KnowledgeCategory(models.Model):
    id = models.SmallAutoField(verbose_name="Knowledge category", primary_key=True)
    name = models.CharField(max_length=255)