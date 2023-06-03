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



class CustomerDetailsAddressSerializer(serializers.ModelSerializer):

    customers_address=GetCustomersSerializer(many=True)
    class Meta :
        model = customers
        fields =(' first_name','last_name','mobile','dob',' addres',' country',' city')