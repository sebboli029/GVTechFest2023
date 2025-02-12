import random

class jugador:
    def __init__(self,nombre,posicion,habilidad_ataque,habilidad_defensa):
        self.nombre = nombre
        self.posicion = posicion
        self.habilidad_ataque = habilidad_ataque
        self.habilidad_defensa = habilidad_defensa

    def tiro_arco (self):
        probabilidad_gol = random.uniform(0.5,1)*self.habilidad_ataque
        return (probabilidad_gol)
    
    def info_jugador (self):
        print(f"El nombre es: {self.nombre} La posicion es: {self.posicion} Su habilidad en ataque es: {self.habilidad_ataque} Su habilidad en defensa es:{self.habilidad_defensa}")

messi = jugador("Leo Messi","DC",100,40)
cristiano= jugador("Cristiano Ronaldo","DC",50,40)
haaland = jugador("Erling Haaland","DC",60,40)

messi.info_jugador()
tiro = messi.tiro_arco() 
print(tiro)

if tiro  > 60:
    print("GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL")
else:
    print("tu tranquilooooooooooooooooo")
