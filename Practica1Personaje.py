import random
import time

class Personaje:
    def __init__(self, nombre, vitalidad):
        self.nombre = nombre
        self.vitalidad = vitalidad
    
    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def esta_vivo(self):
        return self.vitalidad > 0

class Jugador(Personaje):
    def __init__(self, nombre, vitalidad, habilidades):
        super().__init__(nombre, vitalidad)
        self.habilidades = habilidades
    
    def recibir_daño(self, daño):
        self.vitalidad -= daño
        print(f"{self.nombre} recibió {daño} de daño.")
        if self.vitalidad <= 0:
            print(f"{self.nombre} ha muerto")
            return False
        return True

    def contraatacar(self, enemigo):
        if random.random() <= 0.5:
            daño_contraataque = random.randint(10, 25)
            print(f"{self.nombre} realizó un contraataque crítico y causó {daño_contraataque:.0f} de daño")
            enemigo.recibir_daño(daño_contraataque)
        else:
            print(f"{self.nombre} falló al contraatacar")


    def listar_habilidades(self):
        for h in self.habilidades:
            print(f"Puedo {h}")

class Enemigo(Personaje):
    def __init__(self, nombre, vitalidad, daño_min, daño_max, ataque_esp):
        super().__init__(nombre, vitalidad)
        self.daño_min = daño_min
        self.daño_max = daño_max
        self.ataque_esp = ataque_esp
    
    def atacar_jugador(self, jugador):
        danio_ataque = random.randint(self.daño_min, self.daño_max)
        print(f"{self.nombre} ataca a {jugador.nombre} con daño: {danio_ataque}")
        if not jugador.recibir_daño(danio_ataque):
            return False
        if jugador.esta_vivo():
            jugador.contraatacar(self)
        return True

    def recibir_daño(self, daño):
        self.vitalidad -= daño
        print(f"{self.nombre} recibiendo {daño} de daño.")
        if self.vitalidad <= 0:
            print(f"{self.nombre} ha sido derrotado")
            return False
        return True

jugador = Jugador("AllMight", 100, ["atacar", "volar", "esquivar"])
jugador.saludo()
jugador.listar_habilidades()
print("")

enemigo = Enemigo("AFO", 100, 5, 10, 70)

while jugador.esta_vivo() and enemigo.esta_vivo():
    enemigo.atacar_jugador(jugador)
    print(f"| Vitalidad {jugador.nombre}: {jugador.vitalidad} | Vitalidad {enemigo.nombre}: {enemigo.vitalidad} |")
    print(" ")
    if not jugador.esta_vivo():
        break
    time.sleep(2)

if not jugador.esta_vivo():
    print(f"{jugador.nombre} ha muerto")
else:
    print(f"{enemigo.nombre} ha sido derrotado")
print(f"| Vitalidad {jugador.nombre}: {jugador.vitalidad} | Vitalidad {enemigo.nombre}: {enemigo.vitalidad} |")