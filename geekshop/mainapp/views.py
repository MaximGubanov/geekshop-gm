from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
from basketapp.models import Basket
import random



def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []



def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]



def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]

    return same_products



def products(request, pk=None):
    title = 'Каталог'
    products = Product.objects.all().order_by('price')
    links = ProductCategory.objects.all()
    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links': links,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/products.html', context=context)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    context = {
        'title': title,
        'links': links,
        'hot_product': hot_product,
        'same_products': same_products,
        'products': products,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', context=context)



def product(request, pk):
    title = 'Детали'
    product = get_object_or_404(Product, pk=pk)

    context = {
        'title': title,
        'links': ProductCategory.objects.all(),
        'product': product,
        'same_products': get_same_products(product),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', context=context)