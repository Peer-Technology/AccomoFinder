from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from paynow import Paynow
import time
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def paynow_payment(request):
    paynow = Paynow(
    '13098', 
    '890b8862-9e36-440e-abf6-f975ac9a4610',
    'http://192.168.0.103:8000/api/paynow_payment', 
    'http://192.168.0.103:8000/api/paynow_payment'
    )
    email = request.data.get("email")
    # order = request.data.get("order")
    # phone_number = request.data.get("order")
    payment = paynow.create_payment('Order', 'iteemag@live.com')
    payment.add('Payment for stuff', 1)
    response = paynow.send_mobile(payment, '0774845093', 'ecocash')
    print(response.success)
    if(response.success):
        poll_url = response.poll_url
        print("Poll Url: ", poll_url)
        status = paynow.check_transaction_status(poll_url)
        time.sleep(30)
        print("Payment Status: ", status.status)
        return Response({'response': response},
                    status=HTTP_200_OK)
    else:
        return Response({'Response': 'Paynow Responce success False'})
    # if username is None or password is None:
    #     return Response({'error': 'Please provide both username and password'},
    #                     status=HTTP_400_BAD_REQUEST)
    # user = authenticate(username=username, password=password)
    # if not user:
    #     return Response({'error': 'Invalid Credentials'},
    #                     status=HTTP_404_NOT_FOUND)
    # token, _ = Token.objects.get_or_create(user=user)
    

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
