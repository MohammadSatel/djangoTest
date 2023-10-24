from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Product
from .serializer import ProductSerializer
from rest_framework.decorators import api_view




def index(req):
    return JsonResponse('hello', safe=False)




def myProducts(req):
    all_products = ProductSerializer(Product.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)

@api_view(['GET','POST'])
def products(request):
    print(request)
    tempAr=[]
    for prod in Product.objects.all():
        tempAr.append({"description":prod.description,"productName":prod.productName})
    return HttpResponse(tempAr)