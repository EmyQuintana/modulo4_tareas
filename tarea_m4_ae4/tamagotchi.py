class Tamagotchi:
#Atributos:
        #nombre (str): El nombre del Tamagotchi.
        #color (str): El color del Tamagotchi.
        #salud (int): El nivel de salud del Tamagotchi.
        #felicidad (int): El nivel de felicidad del Tamagotchi.

    def __init__(self, nombre, color, felicidad=50, salud= 50, energia=100,caca=False):
        self.nombre = nombre
        self.color = color
        self.felicidad = felicidad
        self.salud = salud
        self.energia = energia
        self.comidas_desde_ultima_caca = 0
        self.tiene_caca = caca
    
    def mostrar_estado(self):
        if self.salud <= 0:
        # Tamagotchi muerto 💀
            estado = "💀 Muerto"

        elif self.felicidad >= 70:
        # Tamagotchi feliz 😊
            estado = "😊 Feliz"
        else:
        # Tamagotchi normal 🙂
            estado = "🙂 Normal"
        print(f"--- {self.nombre} ---")
        print(estado)
    print("------------------")

    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        print(f"\n{self.nombre} está jugando y su felicidad ahora es {self.felicidad}.")
        print(f"La salud de {self.nombre} ha disminuido a {self.salud}.")

    def comer(self):
        self.felicidad += 5
        self.salud += 10
        self.comidas_desde_ultima_caca += 1
        print(f"\n{self.nombre} esta comiendo y su felicidad ahora es {self.felicidad}.")
        print(f"La salud de {self.nombre} ha aumentado a {self.salud}.")
        

        if self.comidas_desde_ultima_caca >= 2:
            self.tiene_caca = True
            print(f"\n Alerta ¡{self.nombre} ha hecho caca! 💩 Toca limpieza")
            self.comidas_desde_ultima_caca = 0

    def limpiar_caca(self):
        if self.tiene_caca:
            print(f"\n{self.nombre} se siente aliviado. Has limpiado la caca. 🧹")
            self.tiene_caca = False  # La caca ha sido limpiada
            self.energia -= 20  # <-- La energía del Tamagotchi disminuye al limpiarla
            self.salud += 10
            print(f"\nLa energía de {self.nombre} ha disminuido a {self.energia}.")
            print(f"La salud de {self.nombre} ha aumentado a {self.salud}.")
        else:
            print(f"No hay caca para recoger.")

    def curar(self):
        self.felicidad += 20
        self.salud -= 25
        print(f"\n{self.nombre} esta curandose y su felicidad ahora es {self.felicidad}.")
        print(f"La salud de {self.nombre} ha disminuido a {self.salud}.")

    def __str__(self):
        return  (f"  Nombre: {self.nombre}\n"
                f"  Salud: {self.salud}\n"
                f"  Felicidad: {self.felicidad}\n"
                f"  Energía: {self.energia}\n")