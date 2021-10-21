from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product


def products(request, pk=None):

    title = 'Каталог'
    products = Product.objects.all().order_by('price')
    links = ProductCategory.objects.all()

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
        }

        return render(request, 'mainapp/products.html', context=context)

    same_products = Product.objects.all()[1:2]
    context = {
        'title': title,
        'links': links,
        'same_products': same_products,
        'products': products,
    }

    return render(request, 'mainapp/products.html', context=context)
