import time
import random

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

    def listar_habilidades(self):
        for h in self.habilidades:
            print(f"Puedo {h}")

    def contraatacar(self, enemigo):
        if random.randint(1, 100) <= 30:
            dano_critico = random.randint(1, 10)
            print(f"¡{self.nombre} ha realizado un contraataque crítico y ha infligido {dano_critico} puntos de daño a {enemigo.nombre}!")
            enemigo.recibir_daño(dano_critico)
        else:
            print(f"{self.nombre} ha intentado contraatacar, pero ha fallado.")

class Enemigo(Personaje):
    def __init__(self, nombre, vitalidad, daño, ataque_esp):
        super().__init__(nombre, vitalidad)
        self.daño = daño
        self.ataque_esp = ataque_esp
    
    def atacar_jugador(self, jugador):
        danio_aleatorio = random.randint(1, 20)
        if danio_aleatorio >= 14:
            danio = 5
            print(f"Enemigo {self.nombre} ha lanzado un ataque especial con daño: {danio}")
        else:
            danio = self.daño
            print(f"Enemigo {self.nombre} atacando a jugador {jugador.nombre} con daño: {danio}")
        jugador.recibir_daño(danio)

jugador = Jugador("Juan", 100, ["atacar", "volar", "esquivar"])
jugador.listar_habilidades()
jugador.saludo()

enemigo = Enemigo("Raul", 50, 10, 70)

while jugador.esta_vivo():
    enemigo.atacar_jugador(jugador)
    print(f"vitalidad {jugador.nombre}: {jugador.vitalidad}")
    time.sleep(2)

    if jugador.esta_vivo():
        jugador.contraatacar(enemigo)
        print(f"vitalidad {enemigo.nombre}: {enemigo.vitalidad}")
        time.sleep(2)

print(f"El jugador {jugador.nombre} ha muerto")
