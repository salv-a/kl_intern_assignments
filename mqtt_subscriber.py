import paho.mqtt.client as mqtt

topic_name=input("Enter topic name:")
def on_connect(client, userdata, flags, rc):
     print("Connected with result code " + str(rc))
     client.subscribe(topic_name)


def on_message(client, userdata, msg):
    print("Received message: " + str(msg.payload.decode()))


client = mqtt.Client()


client.on_connect = on_connect
client.on_message = on_message


broker_address = "localhost"
broker_port = 1883
client.connect(broker_address, broker_port, 60)


client.loop_start()


while True:
    pass
