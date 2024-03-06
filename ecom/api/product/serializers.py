from rest_framework import serializers
from .models import products

class productSerializers(serializers.HyperlinkedModelSerializer):
    image =serializers.ImageField(max_length=None,allow_empty_file=False,allow_null=True,required=False)
    class Meta:
        model = products
        fields = '__all__'