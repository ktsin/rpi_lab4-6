from django.db import models
from .KnowledgeCategory import KnowledgeCategory
from .Author import Author


class Book(models.Model):
    id = models.BigAutoField(verbose_name="Book Id", primary_key=True)
    category_id = models.ForeignKey(KnowledgeCategory, on_delete=models.DO_NOTHING, verbose_name='Category Id')
    authors = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name='Authors')
    name = models.CharField(max_length=255, verbose_name="Book's name")
    publish_date = models.PositiveSmallIntegerField(verbose_name='Year of publishing')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Price')

    def __str__(self):
        return f'{self.name} -- {self.authors}; {self.publish_date} -> {self.category_id.name}'

    def __unicode__(self):
        return self.__str__()