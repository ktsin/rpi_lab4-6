from django.db import models
from .Book import Book
from .KnowledgeCategory import KnowledgeCategory


class BookOutcome(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, verbose_name='Book', null=True)
    category = models.ForeignKey(KnowledgeCategory, on_delete=models.DO_NOTHING, verbose_name='Category')
    out_count = models.PositiveIntegerField(verbose_name='Outcome count')
    out_date = models.DateField(verbose_name="Outcome date")
    out_price = models.DecimalField(verbose_name="Outcome price", max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.book.__str__()} --  {self.out_date} : {self.out_count} = {self.out_price} '

    def __unicode__(self):
        return self.__str__()