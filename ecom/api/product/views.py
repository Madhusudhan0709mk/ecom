from .models import products
from rest_framework import viewsets
from .serializers import productSerializers

class productViewSet(viewsets.ModelViewSet):
    queryset = products.objects.all().order_by('name')
    serializer_class = productSerializers