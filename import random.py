import random

class Personaje:
    def __init__(self):
        self.vida = 100
    
    def danio(self):
        lanzamiento = random.randint(1,20)
        if lanzamiento >= 14:
            self.vida -= 5
            print("¡El ataque ha acertado! La vida del personaje se reduce a", self.vida)
        else:
            print("El ataque ha fallado.")

personaje = Personaje()

print("La vida inicial del personaje es de", personaje.vida)

for i in range(10):
    personaje.danio()
