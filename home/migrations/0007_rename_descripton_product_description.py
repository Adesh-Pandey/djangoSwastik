# Generated by Django 3.2.8 on 2021-11-01 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descripton',
            new_name='description',
        ),
    ]
