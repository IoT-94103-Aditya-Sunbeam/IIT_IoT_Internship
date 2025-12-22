import paho.mqtt.client as mqtt
import random

def on_publish(client, userdata, mid, reason_code, properties):
    print("message is published")

publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

publisher.on_publish = on_publish

publisher.connect("localhost")

ldr_value = random.randint(0,1023)
publisher.publish("sensor/ldr", ldr_value)

publisher.disconnect()