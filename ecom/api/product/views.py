from rest_framework import viewsets
from .serializers import ProductSerializers
from .models import Product
class ProductViewsets(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializers
