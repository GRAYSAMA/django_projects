from django.http import HttpResponse
from django.template import loader
from .models import Products

def products(request):
   myproducts = Products.objects.all().values()
   template = loader.get_template('hello.html')
   context = {
     'myproducts': myproducts,
   }
   return HttpResponse(template.render(context, request))


def details(request, id):
  myproduct = Products.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myproduct': myproduct,
  }
  return HttpResponse(template.render(context, request))