# TC3041-P4-Primavera-2019

## Problema a resolver
Nuestra propuesta es tener un sensor en la bicicleta o un reloj que permita al usuario tener un entrenamiento más personalizado ya que el sensor sabe cuál es tu meta y te indica que tipo de entrenamiento debes realizar (ligero o pesado). El sensor también recopila información de la distancia, las calorias quemadas y la velocidad a la que vas para poder definir si el entrenamiento está funcionando y si está cumpliendo el objetivo de lograr que llegues a tu meta u objetivo propuesto. Este proyecto se desrrolló utilizando Python, InfluxDB y Grafana.

## Las mediciones
Existen tres tipos de mediciones en la base de datos que son:
1. Entrenamientos: 
  Dos tipos que son ligero y pesado
2. Recorridos: 
    Pueden ser calle o pasto
3. Sensores:
    Sensor de bicicleta o sensor de mano (reloj)

## Para poder utilizarlo
Se deben realizar las instrucciones que se encuentran en el archivo comandos.txt y acceder al localhost:3000 para poder visualizar los datos en Grafana.
