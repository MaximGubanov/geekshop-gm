from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from authapp.models import ShopUser
from django.views.generic import ListView
from mainapp.models import ProductCategory, Product
from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm
from adminapp.forms import ProductCategoryEditForm, ProductEditForm
from django.contrib.auth.mixins import LoginRequiredMixin



class UsersListView(LoginRequiredMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data()
        context['title'] = 'админка/пользователи'

        return context

    def get_queryset(self):
        return ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админка/пользователи'
#
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     context = {
#         'title': title,
#         'objects': users_list
#     }
#
#     return render(request, 'adminapp/users.html', context)




@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin_staff:users'))
    else:
        user_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'user_form': user_form
    }

    return render(request, 'adminapp/user_update.html', context)




@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_staff:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    context = {
        'title': title,
        'user_form': edit_form
    }

    return render(request, 'adminapp/user_update.html', context)




@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin_staff:users'))

    context = {
        'title': title,
        'user_to_delete': user
    }

    return render(request, 'adminapp/user_delete.html', context)




@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'админка/категории'

    categories_list = ProductCategory.objects.all()

    context = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', context)




@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'товары/создание'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin_staff:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})

    context = {
        'title': title,
        'product_form': product_form,
        'category': category,
    }

    return render(request, 'adminapp/product_update.html', context)




@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'Категории/редактирование'

    edit_category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:category_update', args=[edit_category.pk]))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)

    context = {
        'title': title,
        'category_form': edit_form
    }

    return render(request, 'adminapp/category_update.html', context)




@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'Категории/удаление'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('adminapp:categories'))

    context = {
        'title': title,
        'category_to_delete': category
    }

    return render(request, 'adminapp/category_delete.html', context)




@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)




@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'Товар/создание'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin_staff:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})

    context = {
        'title': title,
        'product_form': product_form,
        'category': category,
    }

    return render(request, 'adminapp/product_update.html', context)




@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):

    title = 'продукт/подробнее'

    product = get_object_or_404(Product, pk=pk)

    context = {
        'title': title,
        'object': product,
    }

    return render(request, 'adminapp/product_read.html', context)




@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'товары/редактирование'

    edit_product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_staff:product_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    context = {
        'title': title,
        'product_form': edit_form
    }

    return render(request, 'adminapp/product_update.html', context)




@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    title = 'продукт/удаление'

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('admin_staff:products', args=[product.category.pk]))

    context = {
        'title': title,
        'product_to_delete': product,
    }

    return render(request, 'adminapp/product_delete.html', context)


def db_profile_by_type(prefix, type, queries):
    update_queries = list(filter(lambda x: type in x['sql'], queries))
    print(f'db_profile {type} for {prefix}: ')
    [print(query['sql']) for query in update_queries]


@receiver(pre_save, sender=ProductCategory)
def product_is_active_update_productcategory_save(sender, instance, **kwargs):
    if instance.pk:
        if instance.is_active:
            instance.product_set.update(is_active=True)
        else:
            instance.product_set.update(is_active=False)

        db_profile_by_type(sender, 'UPDATE', connection.queries)
