from django.contrib import admin
from .models import Customer,PaymentCustomer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    readonly_fileds =  ('updated', 'created')

class PaymentCustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('updated','created')


admin.site.register(Customer,CustomerAdmin)
admin.site.register(PaymentCustomer,PaymentCustomerAdmin)