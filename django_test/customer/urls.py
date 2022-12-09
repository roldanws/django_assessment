from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import HomePageView,CustomerListView,CustomerDetailView,CustomerCreateView,CustomerUpdateView,CustomerDeleteView,PaymentCustomerListView,PaymentCustomerDetailView

customer_patterns = ([
    path('customers/', login_required(CustomerListView.as_view()), name='customers'),
    path('customer/<int:pk>/<slug:slug>', login_required(CustomerDetailView.as_view()), name='customer'),
    path('create/', login_required(CustomerCreateView.as_view()), name='create'),
    path('update/<int:pk>/', login_required(CustomerUpdateView.as_view()), name='update'),
    path('delete/<int:pk>/', login_required(CustomerDeleteView.as_view()), name='delete'),
    path('payments_customers/', login_required(PaymentCustomerListView.as_view()), name='payments'),
    path('payments_customer/<int:pk>/<slug:slug>', login_required(PaymentCustomerDetailView.as_view()), name='payment'),

], 'customer')