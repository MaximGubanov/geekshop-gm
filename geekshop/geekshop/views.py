from django.shortcuts import render
from mainapp.models import Product, Contacts


def index(request):
    title = 'Магазин'

    products = Product.objects.all()[:3]

    context = {
        'title': title,
        'products': products,
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