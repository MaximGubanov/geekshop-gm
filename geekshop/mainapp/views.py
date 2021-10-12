from django.shortcuts import render
from .models import ProductCategory

def products(request):

    title = 'Каталог'

    links = ProductCategory.objects.all()

    context = {
        'title': title,
        'links': links,
    }
    return render(request, 'mainapp/products.html', context=context)
