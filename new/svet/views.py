from django.shortcuts import render
from django.http import JsonResponse
import paho.mqtt.publish as publish 
# Create your views here.
def control(request, state, led_number):
    topic = "ledcontrol"
    message = str(state)
    adress = "m2.wqtt.ru"
    portmqtt = 19773
    mqtt_auth = {
        "username": "u_S05TZ5",
        "password": "QBt2pRBO"
    }
    try:
        publish.single(f"u_S05TZ5/ledcontrol", payload=message, hostname=adress, port=portmqtt, auth=mqtt_auth)
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