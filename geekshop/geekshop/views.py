from django.shortcuts import render
from mainapp.models import Product, Contacts
from basketapp.models import Basket


def index(request):
    title = 'Магазин'
    basket = Basket.objects.filter(user=request.user)

    products = Product.objects.all()[:3]

    context = {
        'title': title,
        'products': products,
        'basket': basket,
    }

    return render(request, 'geekshop/index.html', context=context)

def contacts(request):
    title = 'Контакты'

    contacts = Contacts.objects.all()

    context = {
        'title': title,
        'contacts': contacts
    }

    return render(request, 'geekshop/contact.html', context=context)