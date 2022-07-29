from django_ledger.forms.mpesa_form import Mpesa_form
import datetime 
import math
from django.http import HttpResponse
from django.shortcuts import redirect, render
from requests.auth import HTTPBasicAuth
import json
import requests
from django.contrib.auth.decorators import login_required

'''
def getAccessToken(request):
    consumer_key = 'XjWEg9z1ihL9zoXO1JRaCOhfIJAgB8cu'
    consumer_secret = 'y48BAeDDA0AgXqI2'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)

@login_required
def mpesa(request):
    transaction_id = datetime.datetime.now().timestamp()
    if request.user.is_authenticated:
        client=request.user
    form=Mpesa_form()
    if request.method=='POST':
        form=Mpesa_form(request.POST)
        if form.is_valid():
            form.save()
            Amount=str(form.cleaned_data['amount'])
            number='254'+str(form.cleaned_data.get('phone'))
            print(number+' Amount '+Amount)

            access_token = MpesaAccessToken.validated_mpesa_access_token
            api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization": "Bearer %s" % access_token}
            request = {
                "BusinessShortCode": Lipa_na_Mpesa_Password.Business_short_code,
                "Password": Lipa_na_Mpesa_Password.decode_password,
                "Timestamp": Lipa_na_Mpesa_Password.lipa_time,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": Amount,
                "PartyA":  number,  # replace with your phone number to get stk push -600989
                "PartyB": Lipa_na_Mpesa_Password.Business_short_code,
                "PhoneNumber": number,  # replace with your phone number to get stk push
                "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
                "AccountReference": "Mania",
                "TransactionDesc": "Fear not for I am with you"
            }
            response = requests.post(api_url, json=request, headers=headers)
            print(response)
            return HttpResponse('success')
            #return redirect('paymentcomplete')
    context={'form':form}
    return render(request, 'django_ledger/mpesa/mpesa_client.html')


# The last page
def thankspayment(request):
    t_time = datetime.datetime.now()
    hours = 0.5
    added_time = datetime.timedelta(hours=hours)
    time = t_time + added_time
    print(time)

    context = {'time': time}
    return render(request, 'django_ledger/mpesa/mpesa_thanks.html', context)

'''

import math

from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
from requests.auth import HTTPBasicAuth
import datetime
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword


def getAccessToken(request):
    consumer_key = 'XjWEg9z1ihL9zoXO1JRaCOhfIJAgB8cu'
    consumer_secret = 'y48BAeDDA0AgXqI2'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)


def mpesa(request):

    transaction_id = datetime.datetime.now().timestamp()
    if request.user.is_authenticated:
        client=request.user
    form=Mpesa_form()
    if request.method=='POST':
        form=Mpesa_form(request.POST)
        if form.is_valid():
            form.save()
            Amount=str(form.cleaned_data['amount'])
            number='254'+str(form.cleaned_data.get('phone'))
            print(number+' Amount '+Amount)
            access_token = MpesaAccessToken.validated_mpesa_access_token
            api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization": "Bearer %s" % access_token}
            request = {
                "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
                "Password": LipanaMpesaPpassword.decode_password,
                "Timestamp": LipanaMpesaPpassword.lipa_time,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": Amount,
                "PartyA":  number,  # replace with your phone number to get stk push -600989
                "PartyB": LipanaMpesaPpassword.Business_short_code,
                "PhoneNumber": number,  # replace with your phone number to get stk push
                "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
                "AccountReference": "Mania",
                "TransactionDesc": "Fear not for I am with you"
            }

            response = requests.post(api_url, json=request, headers=headers)
            print(response)
            # return HttpResponse('success')
            return HttpResponse("Django ledger working, Mania you did it")

    ontext={'form':form}
    return render(request, 'django_ledger/mpesa/mpesa_client.html')


# The last page
def thankspayment(request):
    t_time = datetime.datetime.now()
    hours = 0.5
    added_time = datetime.timedelta(hours=hours)
    time = t_time + added_time
    print(time)

    context = {'time': time}
    return render(request, 'django_ledger/mpesa/mpesa_thanks.html', context)