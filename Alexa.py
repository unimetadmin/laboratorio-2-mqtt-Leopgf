import requests
import json
import sys
import time
import numpy as np
import paho.mqtt.client
import paho.mqtt.publish
import Sus


def on_connect(client, userdata, flags, rc):
    print('Alexa conectada')


def main():
    client = paho.mqtt.client.Client("Clima", False)
    client.qos = 0
    client.connect(host='localhost')
    url = "http://api.openweathermap.org/data/2.5/weather?lat=10.491&lon=-66.902&appid=ddaf75c29a859c87c07b70802fc501e8"
    var = time.time()
    var2 = time.time()

    while True:
        res = (requests.get(url)).json()
        tiemp = int(var - var2)
        if res["cod"] != "404":

            clima2 = res["main"]

            current_temperature = int(clima2["temp"])
            temp_celcius = (current_temperature - 273)
            item = {
                "data": str("La temperatura de Caracas es " + str(temp_celcius) + "C"),
                "tipo": 5
            }
            payload = {
                "valor": temp_celcius,
                "tiempo": tiemp,
                "item": item
            }
            client.publish('casa/sala/alexa_echo', json.dumps(payload), qos=0)

        else:
            print(" City Not Found ")
        time.sleep(600)
        var = time.time()


if __name__ == '__main__':
    main()
    sys.exit(0)

