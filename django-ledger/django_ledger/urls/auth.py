from django.urls import path

from django_ledger import views
from django_ledger.views import mpesa_payment 

urlpatterns = [
    path('login/', views.DjangoLedgerLoginView.as_view(), name='login'),
    path('logout/', views.DjangoLedgerLogoutView.as_view(), name='logout'),
 path('mpesa/', mpesa_payment.getAccessToken, name='mpesa'),
    #path('lipa', views.lipa_na_mpesa_online, name='lipa'),
path('pay', mpesa_payment.mpesa, name='pay'),
    path('paymentcomplete/', mpesa_payment.thankspayment, name='paymentcomplete'),
]