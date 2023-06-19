from django.shortcuts import render
from django.http import JsonResponse
from user_app.models import Account
from menu_app.models import Product


def show_main(request):
    context = {}
    all_products = Product.objects.all()
    context['all_products'] = all_products

    return render(request, 'main.html', context)
