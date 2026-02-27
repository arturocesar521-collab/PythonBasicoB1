from Enemigo import *
import random
class Ogro(Enemigo):
    def __init__(self, puntos_energia=20, ataques=3):
        super().__init__(tipo_enemigo='Ogro', puntos_energia=puntos_energia, ataque=ataques)

    def habla(self):
        print("ogro aplasta todo!!!")

    def ataque_especial(self):
        print("Ogro ataque especial")
        funcion_ataque_especial = random.random() < 0,20
        if funcion_ataque_especial:
            self.ataque += 4
            print('Ogro enojado y incemento su ataque por 4!!!')
