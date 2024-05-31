from django.urls import path,re_path,include
from . import views

urlpatterns = [
    path('', views.Wallet.as_view() ),
    path('<pk>', views.WalletDelete.as_view() ),
]