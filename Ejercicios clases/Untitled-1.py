class Animal:
    def __init__(self, nombre, raza, color):
        self.nombre = nombre
        self.raza = raza
        self.color = color

    def hacer_truco(self):
        print(f"{self.nombre} hace un truco")


class Perro(Animal):
    def __init__(self, nombre, raza, color, altura):
        super().__init__(nombre, raza, color)
        self.altura = altura
    def hacer_truco(self):
        print(f"{self.nombre} salta sobre su altura {self.altura} cm")


class Gato(Animal):

    def __init__(self, nombre, raza, color, razcar):
        super().__init__(nombre, raza, color)
        self.razcar = razcar
    def hacer_truco(self):
        print(f"{self.nombre} rasca {self.razcar} veces")


class Gato_Angora(Gato):

    def __init__(self, nombre, raza, color, razcar, altura):
        super().__init__(nombre, raza, color, razcar)
        self.altura = altura
    
    def hacer_truco(self):
        print(f"{self.nombre} salta y rasca {self.razcar} veces a una altura de {self.altura} cm")

camaleon = Animal("Camaleón", "Reptil", "Verde")
camaleon.hacer_truco()

perro = Perro("Chocolo", "Labrador", "Marrón", 60)
perro.hacer_truco()

gato = Gato("Miau", "Siames", "Gris", 5)
gato.hacer_truco()

kitty = Gato_Angora("Kitty", "Angora", "Blanco", 3, 50)
kitty.hacer_truco()