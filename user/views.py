import requests

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def activate_user(req,uid,token):
    if uid and token:
        data = {'uid':uid,'token':token}
        url = 'http://localhost:8000/api/auth/users/activation/'
        activate = requests.post(url,data=data)
        return Response({'success':activate},status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'uid and token failure'},status=status.HTTP_417_EXPECTATION_FAILED)
    
@api_view(['GET','POST'])
def password_reset_confirm(request,uid,token):
    if request.method == 'POST':
        post_uid = request.data.get('uid')
        post_token = request.data.get('token')
        post_new_password = request.data.get('new_password')
        data={
            "uid": post_uid,
            "token": post_token,
            "new_password": post_new_password
        }
        url = 'http://localhost:8000/api/auth/users/reset_password_confirm/'
        password_reset = requests.post(url,data=data)
        return Response({'success':password_reset},status=status.HTTP_201_CREATED)
    return Response({'UID': uid, 'TOKEN': token},status=status.HTTP_200_OK)

@api_view(['POST'])
def password_reset_confirm_2(request):
    post_uid = request.data.get('uid')
    post_token = request.data.get('token')
    post_new_password = request.data.get('new_password')
    if post_uid and post_token and post_new_password:
        data={
            "uid": post_uid,
            "token": post_token,
            "new_password": post_new_password
        }
        url = 'http://localhost:8000/api/auth/users/reset_password_confirm/'
        password_reset = requests.post(url,data=data)
        return Response({'success':password_reset},status=status.HTTP_201_CREATED)