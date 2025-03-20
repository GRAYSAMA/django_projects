from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Products


def products(request):
    myproducts = Products.objects.all().values()
    context = {
        'myproducts': myproducts
    }
    return render(request, 'hello.html', context)


def details(request, id):
  myproduct = Products.objects.get(id=id)
  context = {
    'myproduct': myproduct,
  }
  return render(request,'details.html', context)


def main(request):
    return render(request, 'main.html') 