# Generated by Django 5.0 on 2023-12-17 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True, unique=True),
        ),
    ]
