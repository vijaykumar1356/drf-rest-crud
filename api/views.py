
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

from .serializers import ProductSerializer
from .models import Product


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'USER LIST': '/user',
        'USER': '/user/<str:uuid>',
        'CREATE': '/user',
        'UPDATE': '/user/<str:uuid>',
        'DELETE': '/user/<str:uuid>'
    }
    return Response(api_urls)


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def productCrud(request, uuid=None):
    if request.method == 'GET' and not uuid:
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and uuid:
        product = Product.objects.get(uuid=uuid)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        product = Product.objects.get(uuid=uuid)
        product.delete()
        return Response(status=204)

    if request.method == 'PUT':
        product = Product.objects.get(uuid=uuid)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
