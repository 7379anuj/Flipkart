from django.urls import path,include
from customer.views import *
urlpatterns = [
    path('get-customers',GetCustomersView.as_view()),
    path('get-customersAddress',GetCustomerAddressView.as_view()),
    path('get-details',CustomerDetailsAddressView.as_view())
]