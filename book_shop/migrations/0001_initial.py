# Generated by Django 3.2 on 2021-04-26 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeCategory',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Knowledge category')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
