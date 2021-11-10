from django.db import models

# Create your models here.


class Contact (models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    desc = models.TextField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.name


class Slide(models.Model):

    image = models.ImageField(upload_to="pics", default="")
# , height_field=300, width_field=1000


class HomeData(models.Model):
    title = models.CharField(max_length=300, blank=True)
    paragraph = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="pics", default="", blank=True)

    def __str__(self):
        return self.title + self.paragraph[0:10]


class AboutData(models.Model):
    title = models.CharField(max_length=300, blank=True)
    paragraph = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="pics", default="", blank=True)

    def __str__(self):
        return self.title+self.paragraph[0:10]


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)
    favourite = models.BooleanField(default=False)
    image = models.ImageField(upload_to="pics", default="")

    def __str__(self):
        return self.name
