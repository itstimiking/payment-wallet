from django.urls import path,re_path,include
from . import views

urlpatterns = [
    path('activate/<str:uid>/<str:token>', views.activate_user ),
    path('password-reset-confirm/<str:uid>/<str:token>', views.password_reset_confirm ),   
    path('password-reset-confirm/', views.password_reset_confirm_2 ),   
]