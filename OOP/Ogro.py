from Enemigo import *

class Ogro(Enemigo):
    def __init__(self, puntos_energia=20, ataques=3):
        super().__init__(tipo_enemigo='Ogro', puntos_energia=puntos_energia, ataque=ataques)

    def habla(self):
        print("ogro aplasta todo!!!")