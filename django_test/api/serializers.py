from rest_framework import serializers
from customer.models import Customer, PaymentCustomer
from rest_framework.serializers import ModelSerializer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'