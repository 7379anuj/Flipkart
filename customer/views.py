from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from customer.models import *
from customer.serializers import *
# Create your views here.
class GetCustomersView(APIView):
    def get(self,request):
        instance = customers.objects.all()
        serializer = GetCustomersSerializer(instance,many=True)
        return Response(serializer.data)
    def post(self,request):
        param = request.data
        print("data-",param)
        ser =GetCustomersSerializer(data=param)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({"Message":"Save Successfully"})
    

class GetCustomerAddressView(APIView):
    def get(self,request):
        instance = CustomersAddress.objects.all()
        ser= GetCustomersAddressSerializer(instance,many=True)
        return Response(ser.data)
    

    
class GetCustomerDetailsAddressView(APIView):
    def get(self,request,pk):
         instance = customers.objects.filter(id=pk)
         ser=GetCustomerDetailsAddressSerializer(instance,many=True)
         return Response(ser.data)
        



