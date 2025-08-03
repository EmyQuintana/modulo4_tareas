class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre_jugador = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi

    def jugar_con_tamagotchi(self):
        self.tamagotchi.jugar()  #jugar_con_tamagotchi(): juega e invoca el método de tamagotchi jugar()
    def darle_comida(self):
        self.tamagotchi.comer() #darle_comida(): le da de comer su tamagotchi invocando al método de tamagotchi comer()
        
    def curarlo(self): 
        self.tamagotchi.curar() #curarlo(): sana las heridas de su tamagotchi invocando al método de tamagotchi curar()

    def limpiar_caca_tamagotchi(self):
        print(f"{self.nombre_jugador} está limpiando a {self.tamagotchi.nombre}.")
        self.tamagotchi.limpiar_caca()