from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.
def control(request, state, led_number):
    p = f"led{led_number}{state}"
    url = f"http://192.168.1.73/{p}"
    response = requests.get(f"http://192.168.1.73/{p}")
    return JsonResponse({
        "status": "succes",
        "response": response.text,
    })