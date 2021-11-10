# Generated by Django 3.2.8 on 2021-11-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_descripton_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutdata',
            name='image',
            field=models.ImageField(default='', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='homedata',
            name='image',
            field=models.ImageField(default='', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='aboutdata',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='homedata',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]