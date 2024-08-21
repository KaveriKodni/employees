from rest_framework import serializers
from api.models import Company

#create serializers 
class Company_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields="__all__"

        