from django.db import models
from login.models import User
from .utils import unique_order_id_generator
from django.db.models.signals import pre_save
class Insurance(models.Model):
    policy_name=models.CharField(max_length=30)
    type_of_policy=models.CharField(max_length=30)
    start_date=models.DateField()
    end_date=models.DateField()
    life_assureddetails=models.CharField(max_length=50)
    payment_information=models.IntegerField()
    premium_details=models.IntegerField()
    user_id =models.ForeignKey(
        'login.User',
        on_delete=models.CASCADE,
    )
    policy_created_time=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    insurance_policy_id=models.CharField(max_length=120,blank=True,primary_key=True)
    def __str__(self):
        return self.insurance_policy_id

def pre_save_create_policy_id(sender, instance, *args, **kwargs):
    if not instance.insurance_policy_id:
        instance.insurance_policy_id= unique_order_id_generator(instance)


pre_save.connect(pre_save_create_policy_id, sender=Insurance)
