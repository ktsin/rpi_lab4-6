# Generated by Django 3.2 on 2021-04-26 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledgecategory',
            name='id',
            field=models.SmallAutoField(primary_key=True, serialize=False, verbose_name='Knowledge category'),
        ),
    ]