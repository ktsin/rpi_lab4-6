from django.db import models
from .Book import Book
from .KnowledgeCategory import KnowledgeCategory


class BookIncome(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, verbose_name='Book')
    category = models.ForeignKey(KnowledgeCategory, on_delete=models.DO_NOTHING, verbose_name='Category')
    in_count = models.PositiveIntegerField(verbose_name='Income count')
    in_date = models.DateField(verbose_name="Income date")