from rest_framework import serializers
from customer.models import *
from customer.models import *

class GetCustomersSerializer(serializers.ModelSerializer):
    class Meta :
        model =  customers
        fields ="__all__"



class GetCustomersAddressSerializer(serializers.ModelSerializer):
    class Meta :
        model = CustomersAddress
        fields ="__all__"



class GetCustomerDetailsAddressSerializer(serializers.ModelSerializer):
    customer_addresses=GetCustomersAddressSerializer(many=True)

    class Meta :
        model = customers
        fields =('first_name','last_name','mobile','dob','country','city','customer_addresses')