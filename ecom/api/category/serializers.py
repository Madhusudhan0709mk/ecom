from rest_framework import serializers
from .models import category
# Create your views here.

class categorySerliazier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = category
        fields = ['name','description']