from django.shortcuts import render
from django.http import JsonResponse
import paho.mqtt.publish as publish 
# Create your views here.
def control(request, state, led_number):
    topic = "ledcontrol"
    message = str(state)
    p = f"led{led_number}{state}"
    url = f"http://192.168.1.73/{p}"
    try:
        publish.single(topic, message, hostname="host.docker.internal", port=1883)
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        })
    return JsonResponse({
        "status": "succes",
        "topic": topic,
        "message": message
    })