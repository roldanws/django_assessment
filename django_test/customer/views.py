from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Customer, PaymentCustomer
from administrator.models import Administrator
from .forms import CustomerForm
from random import randrange, choice
# Create your views here.

class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    
class HomePageView(TemplateView):
    """Clase que renderiza el index del sistema"""
    template_name = 'index.html'
    
class CustomerListView(ListView):
    model = Customer
    
    def get_queryset(self):
        # usuario = self.request.user
        customer=Customer.objects.all()
        # print("Usuario y cliente: ", usuario, customer)
        return customer

    
    def get_context_data(self, **kwargs):
        administrator=Administrator.objects.all()
        print("Objects: ", administrator)
        usuario_actual = self.request.user
        print("usuario actual: ", usuario_actual, usuario_actual.id)
        usuario_administrador = Administrator.objects.filter(id=usuario_actual.id)
        #print(usuario_administrador[0].rol)
        context = super().get_context_data(**kwargs)
        try:
            rol = usuario_administrador[0].rol
            nombre = usuario_administrador[0].usuario
            context['rol']=rol
            context['username']=nombre
        except: 
            return context
        # transaccion=self.get_queryset()
        
        # exitosos = transaccion.filter(codigo = 1).count()
        # incidencias = transaccion.filter(codigo__range=(2, 4)).count()
        # no_registrados = transaccion.filter(registrado=False).count()
        # cancelados = transaccion.filter(codigo = 5).count()
        # ingreso=transaccion.filter(codigo__lt=5).aggregate(Sum('monto'))['monto__sum']
        # operaciones = transaccion.count()
        # print("Transaccion full: ",transaccion)

        context['rol']=rol
        context['username']=nombre

        # context['incidencias']=incidencias
        # context['cancelados']=cancelados
        # context['no_registrados']=no_registrados
        # context['ingreso']=ingreso
        # context['operaciones']=operaciones
        """
        try:
            context['diferencia']=int(boletaje)-int(recuperados)-int(tolerancias)-int(locatarios)
        except:
            pass
        """
        return context

class CustomerDetailView(DetailView):
    model = Customer

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customer:customers')

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        if self.success_url:
            url = self.success_url.format(**self.object.__dict__)
                
            payments = PaymentCustomer
            for i in range(2):
                amount = randrange(1, 500, 1)
                product_name = choice(["pro1", "pro2", "pro3","pro4","pro5"])        
                quantity = randrange(1, 500, 1)
                print("Payment: ",amount,product_name, quantity)
                pagos = payments.objects.create( amount=amount, product_name=product_name, quantity=quantity)
        else:
            try:
                url = self.object.get_absolute_url()
            except AttributeError:
                raise ImproperlyConfigured(
                    "No URL to redirect to.  Either provide a url or define"
                    " a get_absolute_url method on the Model."
                )
        return url

    def get_initial(self):
        """Return the initial data to use for forms on this view."""
        return self.initial.copy()

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('customer:update', args=[self.object.id]) + '?ok'

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer:customers')

class PaymentCustomerListView(ListView):
    model = PaymentCustomer

class PaymentCustomerDetailView(DetailView):
    model = PaymentCustomer
