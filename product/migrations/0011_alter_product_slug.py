# Generated by Django 4.0.4 on 2022-04-27 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
