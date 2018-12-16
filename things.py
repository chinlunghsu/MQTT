import paho.mqtt.client as mqtt
import re
import httplib, urllib
import socket
import sys
import time

################################################################
# Please configure the following settings for your environment

MQTT_SERVER = "gpssensor.ddns.net"
MQTT_PORT = 1883
MQTT_ALIVE = 90
MQTT_TOPIC = "LASS/Test/PM25"
SERIALPORT="/dev/ttyS0"
BUADRATE=57600
################################################################

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("MQTT Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print("mqtt payload=%s" %(msg.payload))
    items = re.split('\|',str(msg.payload))
    for item in items:
        if item == '':
            continue 
        pairs = re.split('=',item)
        if (len(items)==1):
            continue
        if (pairs[0] == "device_id"):
            value_devId = pairs[1]
        elif (pairs[0] == "s_d0"):
            value_pm25 = pairs[1]
        elif (pairs[0] == "s_t0"):
            value_temperature = pairs[1]
        elif (pairs[0] == "s_h0"):
            value_humidity = pairs[1]
        elif (pairs[0] == "s_d1"):
            value_pm10 = pairs[1]       

    try:
        if (value_devId == LASS_DEVICE_ID):
            # print "Got the data from %s temperature is %s humidity is %s pm2.5 is %s pm10 is %s" % (LASS_DEVICE_ID, value_temperature, value_humidity, value_pm25, value_pm10)
            s.write(str(value_pm25))
            time.sleep(30)  # sleep 30 seconds
    except:
         return
    
LASS_DEVICE_ID = sys.argv[1]

s=None
import serial
s = serial.Serial(SERIALPORT,BUADRATE)
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqtt_client.loop_forever()
