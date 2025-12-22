import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"message :{message.payload}")

subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

subscriber.on_message = on_message

subscriber.connect("localhost")

subscriber.subscribe("sensor/ldr")

subscriber.loop_forever()
