# Generated by Django 5.1.3 on 2024-11-07 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]