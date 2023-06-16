from django.shortcuts import render
from django.http import JsonResponse
from user_app.models import Account


def show_main(request):
    context = {}


    return render(request, 'main.html', context)
