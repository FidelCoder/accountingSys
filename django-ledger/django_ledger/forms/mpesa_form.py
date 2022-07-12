
from django_ledger.models.mpesa import Mpesa_Transaction
from django.forms import ModelForm
class Mpesa_form(ModelForm):
    class Meta:
        model=Mpesa_Transaction
        fields=["phone", "amount"]