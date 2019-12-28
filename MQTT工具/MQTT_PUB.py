import time
import json
import paho.mqtt.client as mqtt
import random

client = mqtt.Client()

mqtt_username = "admin"
mqtt_password = "admin"
HOST = "49.4.65.143"

# mqtt_username = "admin"
# mqtt_password = "admin"
# HOST = "47.108.50.121"

client.username_pw_set(mqtt_username, mqtt_password)

client.connect(HOST, 1883, 60)

while True:
    # data = {
    #     "co2": random.randint(500, 3000),
    #     "hum": random.randint(0, 100),
    #     "tem": random.randint(0, 50),
    # }

    client.publish("motorAvailability", "online")
    time.sleep(30)
