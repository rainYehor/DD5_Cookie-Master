from django.shortcuts import render
from .models import *
from user_app.models import Account, CartItem
from django.http import JsonResponse
# from FlareRestaurant.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
# from telegram import send_message_tg

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
        counter_price = product_in_cart.product.price * product_in_cart.count
        full_price += counter_price
        product_in_cart.counter_price = counter_price
    context['full_price'] = full_price

    user_order = ''
    for product_index, product_in_cart in enumerate(products_in_cart):
        user_order += f'{product_in_cart.product.name} у кількості: {[product_in_cart.count]}'
        if len(products_in_cart)-1 != product_index:
            user_order += '); '
        else:
            user_order += ')'
    
    message = f"Новий заказ!\nІм'я:{account.name}.\nЗаказ:{user_order}.\nЗагальна ціна:{full_price}грн"
    print(message)
    # CartItem.objects.all().delete()
    # send_message_tg(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, message)
    return render(request, 'cart.html', context)


def delete_from_cart(request):
    # pass
    if request.method == 'POST':
        account = Account.objects.get(email = request.user)
        # print(request.POST.get("cartItemId"))
        # cart_item = CartItem.objects.get(id = request.POST.get("cartItemId"))
        # cart_item.delete()

        # print(product_in_cart)

        CartItem.objects.get(pk = request.POST.get('cartItemId')).delete()
        print(request.POST, 'text')
    return JsonResponse({})

def order_processing(request):
    context = {}
    account = Account.objects.get(user = request.user)
    cartItems = CartItem.objects.filter(account = account)
    delete_from_cart(request)
    products_in_cart = cartItems
    context['products_in_cart'] = products_in_cart
    full_price = 0
    for product_in_cart in products_in_cart:
        counter_price = product_in_cart.product.price * product_in_cart.count
        full_price += counter_price
        product_in_cart.counter_price = counter_price
    context['full_price'] = full_price
    return render(request, 'order.html')