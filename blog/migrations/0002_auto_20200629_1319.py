# Generated by Django 2.2.13 on 2020-06-29 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=models.TextField(default='DEFAULT VALUE', max_length=200),
        ),
    ]
