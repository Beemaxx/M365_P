# Generated by Django 4.0.4 on 2022-04-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='product'),
        ),
    ]