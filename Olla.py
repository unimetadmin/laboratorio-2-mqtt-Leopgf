import json
import sys
import time
import numpy as np
import paho.mqtt.client
import paho.mqtt.publish
import Sus


def on_connect(client, userdata, flags, rc):
    print('Olla conectada')


def main():
    client = paho.mqtt.client.Client("temperatura", False)
    client.qos = 0
    client.connect(host='localhost')
    min = 0
    max = 150
    alerta = "el agua esta hirviendo"
    var = time.time()
    var2 = time.time()
    tipo = 3
    while True:
        temperatura = int(np.random.uniform(min, max))
        en_usuo = int(np.random.uniform(0, 2))
        tiemp = int(var - var2)
        if en_usuo == 1:
            if temperatura >= 100:
                item = {
                    "data": str("la temperatura de la olla es %s y el agua esta hirviendo" % temperatura),
                    "tipo": tipo
                }
                payload = {
                    "valor": temperatura,
                    "alerta": alerta,
                    "tiempo": tiemp,
                    "item": item,
                }
                client.publish('casa/cocina/temperatura_olla', json.dumps(payload), qos=0)
                print(alerta)
            else:
                item = {
                    "data": str("la temperatura de la olla es %s" % temperatura),
                    "tipo": tipo
                }
                payload = {
                    "valor": temperatura,
                    "tiempo": tiemp,
                    "item": item
                }
                client.publish('casa/cocina/temperatura_olla', json.dumps(payload), qos=0)

            # query = '''insert into suscripcion(tipo_suscripcion_id, descripcion) values(3, %(data)s);'''
            # Sus.on_connect_db(query, item)
            time.sleep(1)
            var = time.time()


if __name__ == '__main__':
    main()
    sys.exit(0)
