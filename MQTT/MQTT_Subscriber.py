import paho.mqtt.client as paho
import time
import sys
import datetime
import time
broker="localhost"  #host name
topic="test"
        
def on_message(client, userdata, message):
  print("received data is :")  
  print(str(message.payload.decode("utf-8")) ) #printing Received message
  print("")
    
client= paho.Client("user") #create client object 
client.on_message=on_message
   
print("connecting to broker host",broker)
client.connect(broker)#connection establishment with broker
print("subscribing begins here")    
client.subscribe(topic)#subscribe topic test

while 1:
    client.loop_start() #contineously checking for message 
