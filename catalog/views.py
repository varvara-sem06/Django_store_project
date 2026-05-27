from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Product
from .forms import ProductForm


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print("=" * 50)
        print(f"Сообщение от {name}")
        print(f"Email: {email}")
        print(f"Сообщение: {message}")  # ✅ исправлено: добавлена f
        print("=" * 50)

        return render(request, 'catalog/contacts.html', {'success': True})

    return render(request, 'catalog/contacts.html')


def product_detail(request, product_id):
    """Отображение детальной информации о товаре"""
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'catalog/product_detail.html', context)


def product_list(request):
    """Отображает список всех товаров"""
    products = Product.objects.all().select_related('category')

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'catalog/product_list.html', context)


def product_create(request):
    """Создание нового товара"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', product_id=product.id)
        else:
            return render(request, 'catalog/product_form.html', {'form': form})
    else:
        form = ProductForm()

    return render(request, 'catalog/product_form.html', {'form': form})
