# Generated by Django 3.2.3 on 2021-05-17 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_shop', '0006_auto_20210503_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('rl', models.CharField(choices=[('ADMIN', 'Admin'), ('BASE', 'Base user')], max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
