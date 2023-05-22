import paho.mqtt.client as mqtt


client = mqtt.Client()


broker_address = "localhost"
broker_port = 1883
client.connect(broker_address, broker_port, 60)

topic = input("Enter topic: ")

while True:
    data = input("Enter message (to quit enter 0): ")
    if data == "0":
        break
    client.publish(topic, data)

client.disconnect()