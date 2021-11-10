from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name='home'),
    path('services/products/<int:counter>/',
         views.services_products, name='services'),
    path('contact', views.contact, name='contact'),
    path('aboutus', views.about, name='aboutus'),
    path("services/products/individualdetails",
         views.individual, name="individual"),
]
