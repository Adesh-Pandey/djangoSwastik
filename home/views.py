from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, HomeData, AboutData, Product, Slide
from django.contrib import messages
# Create your views here.


def index(request):
    allData = HomeData.objects.all()
    images = Slide.objects.all()
    favouriteProduct = Product.objects.all().filter(favourite=True)
    context = {"data": allData, "images": images, "items": favouriteProduct}
    return render(request, "index.html", context)


def about(request):
    allData = AboutData.objects.all()
    context = {"data": allData}
    return render(request, "about.html", context)


def individual(request):
    context = {}
    if(request.method == "POST"):
        context["name"] = request.POST.get("name")
        context["price"] = request.POST.get("price")
        context["description"] = request.POST.get("description")
        context["image"] = request.POST.get("image")

        return render(request, "individual.html", context)
    return render(request, "noservices.html")


def services_products(request, counter):

    if(request.method == "GET" and counter != 0):
        return render(request, "noservices.html")

    if(counter < 0):
        return render(request, "noservices.html")

    allProducts = Product.objects.all()
    items_pre_page = 9
    searchKeyword = ""
    if(request.method == "POST"):
        searchKeyword = request.POST.get("key")
        allProducts = Product.objects.filter(name__icontains=searchKeyword)
        if(len(allProducts) == 0):
            allProducts = Product.objects.all()
            messages.warning(
                request, "Sorry! We are unable to find anything matching. ")
    nextCounter = counter+1
    if(counter == len(allProducts)//items_pre_page):
        nextCounter = 0
        if(counter != 0):
            messages.warning(
                request, "This is the last page! You will be redirected to the first page on pressing NEXT.")
    allProducts = allProducts[counter *
                              items_pre_page:(counter+1)*items_pre_page]

    if(counter == 0):
        prev = counter
    else:
        prev = counter-1
    context = {"products": allProducts,
               "searchKey": searchKeyword, "prevCounter": prev, "nextCounter": nextCounter}

    return render(request, "products.html", context)


def contact(request):
    if(request.method == "POST"):
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")
    context = {"baseUrl": "/static/images/",
               "name": "good_contact"
               }
    return render(request, "contact.html", context)
