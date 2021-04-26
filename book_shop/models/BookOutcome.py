from django.db import models
from .Book import Book
from .KnowledgeCategory import KnowledgeCategory


class BookOutcome(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, verbose_name='Book')
    category = models.ForeignKey(KnowledgeCategory, on_delete=models.DO_NOTHING, verbose_name='Category')
    out_count = models.PositiveIntegerField(verbose_name='Outcome count')
    out_date = models.DateField(verbose_name="Outcome date")
    out_price = models.DecimalField(verbose_name="Outcome price", max_digits=8, decimal_places=2)