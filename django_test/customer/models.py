from django.db import models
from django.utils.timezone import now
# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=200, verbose_name = 'name', null=False, blank=False)
    paternal_surname = models.CharField(max_length=200, verbose_name = 'paternal surname', null=False, blank=False)
    email = models.EmailField(max_length=255, verbose_name = 'email', null=False, blank=False)
    created = models.DateTimeField(verbose_name = 'Fecha creacion', default = now)
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Ultima modificacion')
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['-created']

    def __str__(self):
        return str(self.created.date()) + " " + '(' +str(self.id) + ')'


class PaymentCustomer(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    amount = models.DecimalField(max_digits=5,decimal_places=2, verbose_name = 'amount')    
    product_name = models.CharField(max_length=200, verbose_name = 'product name', null=False, blank=False)
    quantity = models.IntegerField(verbose_name='quantity', null=False, blank=False)
    
    created = models.DateTimeField(verbose_name = 'fecha de creacion', default = now)
    updated = models.DateTimeField(auto_now=True, verbose_name = 'ultima modificacion')
    class Meta:
        verbose_name = 'PaymentCustomer'
        verbose_name_plural = 'PaymentCustomers'
        ordering = ['-created']

    def __str__(self):
        return str(self.id) + " " + str(self.product_name) + " " + str(self.amount) 



