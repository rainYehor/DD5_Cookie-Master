from django.shortcuts import render
from .models import *
from user_app.models import Account, CartItem

# Create your views here.
def show_cart(request):
    context = {}
    account = Account.objects.get(user = request.user)
    cartItems = CartItem.objects.filter(account = account)
    delete_from_cart(request)
    products_in_cart = cartItems
    context['products_in_cart'] = products_in_cart
    full_price = 0
    for product_in_cart in products_in_cart:
        full_price += product_in_cart.product.price
    context['full_price'] = full_price
    return render(request, 'cart.html', context)


def delete_from_cart(request):
    # pass
    if request.method == 'POST':
        account = Account.objects.get(email = request.user)
        cart_item = CartItem.objects.get(id = request.POST.get("cartItemId"))
        cart_item.delete()

        # print(product_in_cart)
        # print(product_in_cart.product.get(pk = request.POST.get('product_pk')))
    