from django.shortcuts import render
from .models import Product


def show_catalog(request):
    context = {}
    products = Product.objects.all()
    context['products'] = products
    response = render(request, 'shop.html', context)

    if request.method == 'POST':
        list_amount_cookie = request.COOKIES.get('amount', '')
        list_product_cookie = request.COOKIES.get('product', '')
        amount = request.POST.get('amount')
        product = request.POST.get('product')


        if list_product_cookie != '':
            list_product = list_product_cookie.split(' ')
            list_amount = list_amount_cookie.split(' ')

            if product in list_product:
                index_product = list_product.index(product)
                list_amount[index_product] = amount
                response.set_cookie('amount', ' '.join(list_amount))
            else:
                response.set_cookie('product', list_product_cookie+' '+product)
                response.set_cookie('amount', list_amount_cookie+' '+amount)
        else:
            response.set_cookie('product', product)
            response.set_cookie('amount', amount)

    return response

 # 
def show_cart(request):
    list_amount_cookie = request.COOKIES.get('amount', '')
    list_product_cookie = request.COOKIES.get('product', '')
    context = {}

    if list_product_cookie != '':
        products = []
        
        list_pk = list_product_cookie.split(' ')
        for pk in list_pk:
            product = {}
            product_name = Product.objects.get(pk = pk).name
            product_description = Product.objects.get(pk = pk).description
            product_image = Product.objects.get(pk = pk).image
            product_price = Product.objects.get(pk = pk).price
            product_pk = Product.objects.get(pk = pk).pk
            list_amount = list_amount_cookie.split(' ')

            for amount in list_amount:
                if list_amount.index(amount) == list_pk.index(pk):
                    product_amount = amount
            product_final_price = int(product_price)*int(product_amount)
            
            product['product_name'] = product_name
            product['product_description'] = product_description
            product['product_image'] = product_image
            product['product_price'] = product_price
            product['product_amount'] = product_amount
            product['product_final_price'] = product_final_price
            product['product_pk'] = product_pk
            products.append(product)

        context['products'] = products

    response = render(request, 'cart.html', context)

    if request.method == 'POST':
        new_list_product = ''
        new_list_amount = ''
        index_product = None
        post_product = request.POST.get('product')
        post_amount = request.POST.get('amount')
        list_product = list_product_cookie.split(' ')
        list_amount = list_amount_cookie.split(' ')

        response = render(request, 'cart.html', context)
        for product in list_product:
            if post_product == product:
                index_product = list_product.index(product)
            if post_product != product:
                if new_list_product != '':
                    new_list_product = new_list_product+' '+product 
                else:
                    new_list_product = new_list_product+product
                print(new_list_product)
        for amount in list_amount:
            if index_product != None:
                print(list_amount.index(amount), index_product)
                if list_amount.index(amount) != index_product:
                    if new_list_amount != '':
                        new_list_amount = new_list_amount+' '+amount
                    else:
                        new_list_amount = new_list_amount+amount

        response.set_cookie('product', new_list_product)
        response.set_cookie('amount', new_list_amount)
    return response