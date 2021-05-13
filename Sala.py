import json
import sys
import time
import numpy as np
import paho.mqtt.client
import paho.mqtt.publish
import Sus


def on_connect(client, userdata, flags, rc):
    print('Sala conectada')


def main():
    client = paho.mqtt.client.Client("Personas", False)
    client.qos = 0
    client.connect(host='localhost')
    alerta = "Hay mas de 5 personas en la sala"

    while True:
        nro_personas = int(np.random.uniform(0, 11))

        if nro_personas > 5:
            item = {
                "data": str(str(alerta) + ", exactamente hay " + str(nro_personas)),
                "tipo": 4
            }
            payload = {
                "valor": str(nro_personas),
                "alerta": alerta,
                "item": item
            }
            client.publish('casa/sala/contador_personas', json.dumps(payload), qos=0)

        time.sleep(60)


if __name__ == '__main__':
    main()
    sys.exit(0)
