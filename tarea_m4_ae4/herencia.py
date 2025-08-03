from tamagotchi import Tamagotchi


class tamagotchi_version_tierno(Tamagotchi):
    def __init__(self, nombre, color, felicidad=50, salud=50, energia=100, caca=False, oler_flores=True): 
        super().__init__(nombre, color, felicidad, salud, energia) 
        self.puede_oler_flores = oler_flores
    def mostrar_info(self):
        return (f"Soy un Tamagotchi de la version tierna llamado {self.nombre}.")
    
    def mostrar_estado(self):
        return super().mostrar_estado()
    def jugar(self):
        return super().jugar()
    def comer(self):
        return super().comer()
    def curar(self):
        return super().curar()
    def limpiar_caca(self):
        return super().limpiar_caca()
    
    def oler_flores_actividad(self):
        if self.puede_oler_flores == True:
            print(f"\n{self.nombre} de la version tierna esta oliendo flores y le suma felicidad")
            self.felicidad += 10    
        else:        
            print(f"{self.nombre} de la version tierna no esta oliendo flores")    

class tamagochi_version_intelectual(Tamagotchi):
    def __init__(self, nombre, color, felicidad=50, salud=50, energia=100, caca=False, aprender= True): 
        super().__init__(nombre, color, felicidad, salud, energia) 
        self.puede_aprender = aprender
    def mostrar_info(self):
        return (f"Soy un Tamagotchi de la version intelectual llamado {self.nombre}.") 
    def mostrar_estado(self):
        return super().mostrar_estado()
    def jugar(self):
        return super().jugar()
    def comer(self):
        return super().comer()
    def curar(self):
        return super().curar()
    def limpiar_caca(self):
        return super().limpiar_caca()
    def aprender_actividad(self):
        if self.puede_aprender == True:
            print(f"\n{self.nombre} esta aprendiendo y le suma felicidad")
            self.felicidad += 10    
        else:        
            print(f"{self.nombre} no esta aprendiendo y le resta salud")
            self.salud -= 5 
            self.felicidad -= 5

class tamagotchi_version_relax (Tamagotchi):
    def __init__(self, nombre, color, felicidad=50, salud=50, energia=100, caca=False, bañarse= True, pasear= True): 
        super().__init__(nombre, color, felicidad, salud, energia) 
        self.bañarse_aguas_termales = bañarse
        self.pasear_bosque = pasear
    def mostrar_info(self):
        return (f"Soy un Tamagotchi de la version relax llamado {self.nombre}.")
    def mostrar_estado(self):
        return super().mostrar_estado()
    def jugar(self):
        return super().jugar()
    def comer(self):
        return super().comer()
    def curar(self):
        return super().curar()
    def limpiar_caca(self):
        return super().limpiar_caca()
    def bañarse_aguas_termales_actividad(self):
        if self.bañarse_aguas_termales == True:
            print(f"\n{self.nombre} esta bañandose en las aguas termales y le suma salud")
            self.salud += 20
        else:        
            print(f"{self.nombre} no esta bañandose y le resta salud")
            self.salud -= 5 
    def pasear_bosque_actividad(self): 
        if self.pasear_bosque == True:
            print(f"\n{self.nombre} esta paseando en el bosque y le suma felicidad")
            self.felicidad += 10    
        else:        
            print(f"\n{self.nombre} no esta paseando y le resta felicidad")
            self.felicidad -= 5
