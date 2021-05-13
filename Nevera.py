import json
import sys
import time
import numpy as np
import paho.mqtt.client
import paho.mqtt.publish
import Sus


def on_connect(client, userdata, flags, rc):
    print('Nevera conectada')


def main():
    client = paho.mqtt.client.Client("Temperatura", False)
    client.qos = 0
    client.connect(host='localhost')
    media = 10
    desEst = 2
    min = 0
    var = time.time()
    var2 = time.time()
    while True:
        tiemp = int(var - var2)
        temperatura = int(np.random.normal(media, desEst))
        hielo = int(np.random.uniform(min, media))

        if tiemp % 300 == 0:
            item = {
                "data": str("La temperatura de la nevera es %s" % temperatura),
                "tipo": 1
            }
            payload = {
                "valor": temperatura,
                "tiempo": tiemp,
                "item": item
            }
            client.publish('casa/cocina/temperatura_nevera', json.dumps(payload), qos=0)

        if tiemp % 600 == 0:
            item = {
                "data": ("La capacidad para generar hielo se encuentra en %s" % hielo),
                "tipo": 2
            }
            payload = {
                "valor": temperatura,
                "hielo": hielo,
                "tiempo": tiemp,
                "item": item
            }
            client.publish('casa/cocina/temperatura_nevera', json.dumps(payload), qos=0)

        time.sleep(1)
        var = time.time()


if __name__ == '__main__':
    main()
    sys.exit(0)
