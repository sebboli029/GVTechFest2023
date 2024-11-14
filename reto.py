import math
import time
import random
from datetime import datetime 
import matplotlib.pyplot as plt

# creando el objeto: sensor
# atributo: tipo, min, max y accion: mide
class Sensor: 
    def __init__(self,tipo,maximo,minimo):
        self.tipo = tipo
        self.maximo = maximo
        self.minimo = minimo

    def medir (self):    
        leer = random.uniform(self.minimo, self.maximo)
        return (leer)

# creando los sensores
LM35  = Sensor("temperatura",5,100)
DHT22  = Sensor("Humedadambiental",30,70)
FC28 = Sensor("Humedadsuelo",50,1000)
BH1750 = Sensor("Intensidadluminica",0,200)

# definir constantes para alarmas
TEMP_BAJA_LM35 = 10 
TEMP_ALTA_LM35 = 24
TEMP_YELLOW_LM35 = 15
HUM_BAJA_DHT22 = 40
HUM_ALTA_DHT22 = 70
HUM_ALTA_FC28 = 34
HUM_BAJA_FC28 = 12
LUZ_ALTA_BH1750 = 150
LUZ_BAJA_BH1750 = 25
LUZ_YELLOW_BH1750 = 75

# creando la lista: lecturas en donde se guradan los valores de los sensores
lecturas = []
timeX = []
temp = []
hsuelo = []
hambiental = []
luz = []

# Añadiendo los valores a la lectura
i = 0
while (i<10):
    valorLM35 = (LM35.medir()*4.88)/10
    valorFC28 = 100-((FC28.medir()/1023)*100)
    valorDHT22 = DHT22.medir()
    valorBH1750 = BH1750.medir()*0.093
    i = i+1
    timestamp = datetime.now()
    lecturas.append(
        {
        "timestamp": timestamp,
        "temperatura": valorLM35,
        "humedadambiental": valorDHT22,
        "humedadsuelo": valorFC28,
        "intensidadluminica": valorBH1750
        }
    )
    time.sleep(1)

# Imprimiendo los valores de los sensores
for dato in lecturas:
    #
    if dato["temperatura"] < TEMP_BAJA_LM35 or dato["temperatura"] > TEMP_ALTA_LM35 : 
        print(f"En la fecha {dato["timestamp"]} se generó una Alerta roja porque la temperatura es {dato["temperatura"]:.2f}°C")
    elif dato["temperatura"] > TEMP_BAJA_LM35 and dato["temperatura"] < TEMP_YELLOW_LM35:
        print(f"En la fecha {dato["timestamp"]} se generó una Alerta amarilla porque la temperatura es {dato["temperatura"]:.2f}°C")
    else:
        print(f"En la fecha {dato["timestamp"]} la temperatura es {dato["temperatura"]:.2f}°C")
        

    #
    if dato["humedadambiental"] < HUM_BAJA_DHT22 or dato["humedadambiental"] > HUM_ALTA_DHT22:
        print(f"En la fecha {dato["timestamp"]} se genero una alerta roja porque la humedad ambiental es {dato["humedadambiental"]:.2f}%")
    else:
         print(f"En la fecha {dato["timestamp"]} la humedad ambiental es {dato["humedadambiental"]:.2f}%")

    if dato["humedadsuelo"] < HUM_BAJA_FC28 or dato["humedadsuelo"] > HUM_ALTA_FC28:
        print(f"En la fecha {dato["timestamp"]} se genero una alerta roja porque la humedad en el suelo es {dato["humedadsuelo"]:.2f}%")
    else:
         print(f"En la fecha {dato["timestamp"]} la humedad en el suelo es {dato["humedadsuelo"]:.2f}%")


    if dato["intensidadluminica"] < LUZ_BAJA_BH1750 or dato["intensidadluminica"] > LUZ_ALTA_BH1750 : 
        print(f"En la fecha {dato["timestamp"]} se generó una Alerta roja porque la temperatura es {dato["intensidadluminica"]:.2f}°C")
    elif dato["intensidadluminica"] > LUZ_BAJA_BH1750 and dato["intensidadluminica"] < LUZ_YELLOW_BH1750:
        print(f"En la fecha {dato["timestamp"]} se generó una Alerta amarilla porque la temperatura es {dato["intensidadluminica"]:.2f}°C")
    else:
        print(f"En la fecha {dato["timestamp"]} la temperatura es {dato["temperatura"]:.2f}°C")

    #
    timeX.append(dato["timestamp"])
    temp.append([dato["temperatura"]])
    hambiental.append(dato["humedadambiental"])
    hsuelo.append(dato["humedadsuelo"])
    luz.append(dato["intensidadluminica"])

# 
plt.subplot(4,1,1)
plt.plot(timeX,temp, color='red', linestyle='--', label='LM35', marker='.', markersize=10, linewidth=2)
plt.title('Temperatura', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})
plt.xlabel('time (seg)')
plt.ylabel('Temperarura en °C')
plt.legend()

plt.subplot(4,1,2)
plt.plot(timeX,hambiental, color='blue', linestyle='--', label='DHT22', marker='.', markersize=10, linewidth=2)
plt.title('Humedad ambiental', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})
plt.xlabel('time (seg)')
plt.ylabel('Humedad ambiental(%)')
plt.legend()

plt.subplot(4,1,3)
plt.plot(timeX,hsuelo, color='Green', linestyle='--', label='FC28', markersize=10, linewidth=2)
plt.title('Humedad en el suelo suelo', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})
plt.xlabel('time (seg)')
plt.ylabel('Huemdad en el suelo(%)')
plt.legend()

plt.subplot(4,1,4)
plt.plot(timeX,luz, color='Grey', linestyle='--', label='BH1750', marker='.', markersize=10, linewidth=2)
plt.title('IntensidadSA', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})
plt.xlabel('time (seg)')
plt.ylabel('Intensidad de luz en FC')
plt.legend()

#Graficar
plt.tight_layout()
plt.show()