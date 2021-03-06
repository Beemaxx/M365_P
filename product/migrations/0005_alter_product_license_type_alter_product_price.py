# Generated by Django 4.0.4 on 2022-04-27 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_vendor_vendorname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='license_type',
            field=models.CharField(choices=[('e-Licence', 'e-Licence'), ('Box', 'Box')], default='e-license', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
