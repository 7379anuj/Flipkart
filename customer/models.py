from django.db import models

# Create your models here.
class customers(models.Model):
    first_name=models.CharField(max_length=15,null=True,blank=True)
    last_name=models.CharField(max_length=15,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    country=models.CharField(max_length=20,null=True,blank=True)
    city=models.CharField(max_length=20,null=True,blank=True)
    dob=models.DateField(max_length=15,null=True,blank=True)
 
    def __str__(self):
        return str(self.first_name)
class CustomersAddress(models.Model):
    customers =models.ForeignKey(customers,on_delete=models.CASCADE,null=True,related_name="customer_addresses")
    street_name=models.CharField(max_length=15,null=True,blank=True)
    street_number=models.IntegerField(max_length=15,null=True,blank=True)
    city=models.CharField(max_length=15,null=True,blank=True)
    state=models.CharField(max_length=15,null=True,blank=True)
    country=models.CharField(max_length=15,null=True,blank=True)
    pincode=models.IntegerField(max_length=15,null=True,blank=True)
    def __str__(self):
        return str(self. street_name)
class CustomersAadhar(models.Model):
        customers =models.OneToOneField(customers,on_delete=models.CASCADE)
        aadhar_number=models.IntegerField(max_length=15,null=True,blank=True)
        aadhar_name=models.CharField(max_length=15,null=True,blank=True)
        def __str__(self):
             return str(self.aadhar_name)
