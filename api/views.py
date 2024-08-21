from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company
from api.serialisers import Company_serializer

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
   queryset=Company.objects.all()
   serializer_class=Company_serializer 