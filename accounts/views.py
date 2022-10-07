from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .helpers import send_otp_to_phone
from .models import User

# Create your views here.


@api_view(['POST'])
def send_otp(request):
    data = request.data

    if data.get('phone_number') is None:
        return Response({
            'status' : 400,
            'message' : 'Phone number is required'
        })


    if data.get('password') is None:
        return Response({
            'status' : 400,
            'message' : 'Password field is required'
        })


    user = User.objects.create(
        username = data.get('username'),
        phone_number = data.get('phone_number'),
        otp = send_otp_to_phone(data.get('phone_number'))
        )
    user.set_password = data.get('set_password')
    user.save()

    return Response({
        'status' : 200,
        'message' : 'OTP has been sent successfully!'
    })



@api_view(['POST'])
def verify_otp(request):
    data = request.data

    if data.get('phone_number') is None:
        return Response({
            'status' : 400,
            'message' : 'Phone number is required'
        })

    if data.get('otp') is None:
        return Response({
            'status' : 400,
            'message' : 'OTP field is required'
        })

    try:
        user_obj = User.objects.get(phone_number = data.get('phone_number'))

    except Exception as e:
        return Response({
            'status' : 400,
            'message' : 'Invalid number'
        })

    if user_obj.otp == data.get('otp'):
        return Response({
            'status' : 200,
            'message' : 'OTP verified!'
        })

    return Response({
        'status' : 400,
        'message' : 'Invalid OTP'
    })
