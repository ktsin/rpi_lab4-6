# Generated by Django 3.2.3 on 2021-05-17 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_shop', '0008_auto_20210517_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='rl',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('BASE', 'Base user')], max_length=100),
        ),
    ]
