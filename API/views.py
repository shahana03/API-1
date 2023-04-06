from django.shortcuts import render
from . models import Product
from . serializer import ProductSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def index(request):
    if request.method=='GET':
        product=Product.objects.all()
        ser=ProductSerializer(product,many=True)
        return JsonResponse(ser.data,safe=False)
    if request.method=='POST':
        ser=ProductSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,status=201)

@api_view(['GET','POST',"DELETE"])
def details(request, id):
    try:
        product=Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({'error':'product not found'}, status=404)
    if request.method=='GET':
        ser=ProductSerializer(product)
        return JsonResponse(ser.data)
    if request.method=='DELETE':
        product.delete()
        return JsonResponse({'DELETED':'Product deleted'},status=204)


