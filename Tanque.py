import sys
import paho.mqtt.client
import paho.mqtt.publish
import time
import numpy as np
import json
import Sus


def vaciar(indicador):
    mean = 10
    std = 5
    capacity = np.random.normal(mean, std)
    indicador -= int(capacity)
    return indicador


def llenar(indicador):
    mean = 20
    std = 5
    capacity = np.random.normal(mean, std)

    indicador += int(capacity)
    return indicador


def reportar(indicador):
    client = paho.mqtt.client.Client("nivel_tanque", False)
    client.qos = 0
    client.connect(host='localhost')

    alertL = "Queda la mitad o menos de agua"
    alertN = "Se acabo el agua"

    if indicador <= 50:
        item = {
            "data": str("Cantidad agua: " + str(indicador) + " " + "Alerta: " + alertL),
            "tipo": 6
        }
        payload = {
            "valor": indicador,
            "alerta": alertL,
            "item": item
        }

    if indicador == 0:
        item = {
            "data": str("Cantidad agua: " + str(indicador) + " " + "Alerta: " + alertN),
            "tipo": 6
        }
        payload = {
            "valor": indicador,
            "alerta": alertN,
            "item": item
        }


def main():
    indicador = 100
    variable = time.time()
    variable2 = time.time()
    while True:
        res = int(variable - variable2)
        if res % 600 == 0:
            indicador = vaciar(indicador)
            reportar(indicador)
        if res % 1800 == 0:
            indicador = llenar(indicador)
        time.sleep(1)
        variable = time.time()


if __name__ == '__main__':
    main()
    sys.exit(0)
