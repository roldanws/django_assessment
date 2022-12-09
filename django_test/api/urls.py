from django.urls import path
from .views import CustomerCreateApiView,CustomerListApiView, CustomerDetailApiView, CustomerUpdateApiView,CustomerDeleteApiView

urlpatterns = [
    path('customers/', CustomerListApiView.as_view(), name='customers'),
    path('customer/<int:pk>/<slug:slug>', CustomerDetailApiView.as_view(), name='customer'),
    path('create/', CustomerCreateApiView.as_view(), name='create'),
    path('update/<int:pk>/', CustomerUpdateApiView.as_view(), name='update'),
    path('delete/<int:pk>/', CustomerDeleteView.as_view(), name='delete'),
]