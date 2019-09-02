import paho.mqtt.client as mqtt

client = mqtt.Client()

mqtt_username = "nas"
mqtt_password = ""
HOST = "192.168.1.100"

client.username_pw_set(mqtt_username, mqtt_password)

client.connect(HOST, 1883, 60)
client.publish("light", "ON")