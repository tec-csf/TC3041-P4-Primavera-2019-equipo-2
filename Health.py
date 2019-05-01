# -*- coding: utf-8 -*-

from time import sleep
from datetime import *
from influxdb import InfluxDBClient
import numpy as np
import random

#Conexión con la base de datos
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'IoT')

#Creación de una base de datos
client.create_database('IoT')

'''times = datetime.utcnow();
for i in range(10):
    times = times + timedelta(minutes = 5)
    times.isoformat()
    print times'''

#distancia(velocidad promedio, superficie y calorias(velocidad promedio), peso ideal

minSpeed = 0.1
maxSpeed = 25.0
minSpeedB = 1.0
maxSpeedB = 40.0
times = datetime.utcnow();
for i in range(8000000):
    random2 = round(random.uniform(minSpeed,maxSpeed+1),2)
    random1 = round(random.uniform(minSpeedB,maxSpeedB+1),2)
    times = times + timedelta(minutes = 1)
    sensores = [{'measurement': 'sensor',
                    'tags':{'tipo':'bicicleta'},
                    'time':times.isoformat(),
                    'fields': {'velocidad':random1}},
                    {'measurement': 'sensor',
                    'tags':{'tipo':'reloj'},
                    'time':times.isoformat(),
                    'fields': {'velocidad':random2}}]
    client.write_points(sensores)
print("Sensor insertado")

minDistance = 0.0
maxDistance = 50.0
times = datetime.utcnow();
for i in range(8000000):
    random1 = round(random.uniform(minDistance,maxDistance+1),2)
    random2 = round(random.uniform(minDistance,maxDistance-4),2)
    times = times + timedelta(minutes = 1)
    recorridos = [{'measurement': 'recorrido',
                'tags':{'terreno':'plano'},
                'time':times.isoformat(),
                'fields': {'distancia':random1}},
                {'measurement': 'recorrido',
                'tags':{'terreno':'pasto'},
                'time':times.isoformat(),
                'fields': {'distancia':random2}}]
    client.write_points(recorridos)
print("Recorrido insertado")

minCalories = 0.0
maxCalories = 2000.0
times = datetime.utcnow();
for i in range(8000000):
    random1 = round(random.uniform(minCalories,maxCalories+1),2)
    random1 = round(random.uniform(minCalories,maxCalories-500),2)
    times = times + timedelta(minutes = 1)
    entrenamientos = [{'measurement': 'entrenamiento',
                      'tags':{'tipo':'pesado'},
                      'time':times.isoformat(),
                      'fields': {'calorias':random1}},
                      {'measurement': 'entrenamiento',
                      'tags':{'tipo':'liviano'},
                      'time':times.isoformat(),
                      'fields': {'calorias':random2}}]
    client.write_points(entrenamientos)
print("Entrenamientos insertado")


