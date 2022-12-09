from django.shortcuts import render
from rest_framework import generics

from .serializers import CustomerSerializer
from Customer.models import Customer

# Create your views here.

class CustomerCreateView(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    
    def get_queryset(self):
        queryset = Customer.objects.all()
        return queryset
