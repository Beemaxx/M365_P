# Generated by Django 4.0.4 on 2022-04-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_productname_product_product_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='amount',
        ),
        migrations.AddField(
            model_name='product',
            name='license_type',
            field=models.CharField(default='e-license', max_length=200),
        ),
    ]
