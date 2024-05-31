from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from rest_framework.response import Response
from . import models, serializers
# Create your views here.


### Wallets ######

class Wallet(generics.ListCreateAPIView):
    queryset = models.WalletModel.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.WalletSerializer
        else:
            return serializers.WalletCreateSerializer
    
class WalletDelete(generics.RetrieveDestroyAPIView):
    queryset = models.WalletModel.objects.all()
    serializer_class = serializers.WalletSerializer
    

### Transactions ######
    
class Transaction(generics.ListCreateAPIView):
    queryset = models.WalletModel.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.WalletSerializer
        else:
            return serializers.WalletCreateSerializer
    
class TransactionsRetrieveUpdateDelete(generics.RetrieveDestroyAPIView):
    queryset = models.WalletModel.objects.all()
    serializer_class = serializers.WalletSerializer