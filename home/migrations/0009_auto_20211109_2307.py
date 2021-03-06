# Generated by Django 3.2.8 on 2021-11-09 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20211109_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='pics')),
            ],
        ),
        migrations.AlterField(
            model_name='aboutdata',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='homedata',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='pics'),
        ),
    ]
