from rest_framework import viewsets
from .serializers import OrderSerializers
from .models import Order

class OrderViewsets(viewsets.ModelViewSet):
    query_set = Order.objects.all().order_by('id')
    serializer_class = OrderSerializers