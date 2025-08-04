from django.db import models

class Collection(models.Model):
    title=models.CharField(max_length=255)


class Product(models.model):
    title=models.CharField(max_length=255)
    description=models.models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    Collection=models.ForeignKey('Collection',on_delete=models.PROTECT)

class customer(models.model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'
    MEMBERSHIP_CHOICES = [
        ("MEMBERSHIP_BRONZE",'Bronze'),
        ("MEMBERSHIP_SILVER",'Silver'), 
        ("MEMBERSHIP_CHOICES",'Gold')
    ]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.models.EmailField(unique=True)
    phone=models.CharField(max_length=255)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default='MEMBERSHIP_BRONZE')

class Order(models.model):
    PAYMENT_STATUS_PENDING='P'
    PAYMENT_STATUS_COMPLETE='C'
    PAYMENT_STATUS_FAILED='F'
    PAYMENT_STATUS_CHOICES=[
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),   
        (PAYMENT_STATUS_FAILED,'Failed')    
    ]
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    
class Address(models.model):
    street=models.models.CharField(max_length=255)
    city=models.models.CharField(max_length=255)
    # customer=models.OneToOneField(customer,on_delete=models.CASCADE, primary_key=True)   #one to on relationship
    customer=models.ForeignKey(
        customer,on_delete=models.CASCADE) 


    
