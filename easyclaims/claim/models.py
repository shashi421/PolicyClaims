from django.db import models
from insurances.models import Insurance
from login.models import User
from .utils import unique_order_id_generator
from django.db.models.signals import pre_save  
 # Create your models her
CLAIM_CHOICES = (
     ('car','Car Claim'),
     ('home', 'Home Claim'),
     ('health','Health Claim'),
    )
 
 # Create your models here.
class Claim(models.Model):
    claim_name=models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=500)
    typeOfClaim=models.CharField(max_length=6, choices=CLAIM_CHOICES, default='')
    details=models.CharField(max_length=500)
    status=models.CharField(max_length=500, default='')
    is_approved=models.BooleanField(default=False)
    policy_id =models.ForeignKey(
        'insurances.Insurance',
        on_delete=models.CASCADE,
             )
    user_id =models.ForeignKey(
        'login.User',
        on_delete=models.CASCADE,
             )
    claim_created_time=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    claim_id=models.CharField(max_length=120,blank=True,primary_key=True)
    def __str__(self):
        return self.claim_id

def pre_save_create_claim_id(sender, instance, *args, **kwargs):
    if not instance.claim_id:
        instance.claim_id= unique_order_id_generator(instance)

pre_save.connect(pre_save_create_claim_id, sender=Claim)

