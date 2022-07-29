
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model



from django.db.models.deletion import CASCADE
from django.db.models.fields import NullBooleanField

user= get_user_model()

class Mpesa_Transaction(models.Model):
    #user=models.ForeignKey(user, on_delete=CASCADE,blank=True,null=True)
    phone=models.IntegerField()
    amount=models.IntegerField()
    transaction_mpesa_id=models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.transaction_mpesa_id
    @property
    def get_total_mpesa_trans(self):
        total_mpesa_transaction=self.mpesa_transaction_set.all()
        sum=0
        total=sum+(single_transaction for single_transaction in total_mpesa_transaction)
        return total




    

