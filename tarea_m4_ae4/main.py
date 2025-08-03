from jugador import Persona
from tamagotchi import Tamagotchi
from herencia import tamagotchi_version_tierno,  tamagotchi_version_relax, tamagochi_version_intelectual

tamagotchi_tierno = tamagotchi_version_tierno("Furawatchi","Rosa")
tamagotchi_intelectual = tamagochi_version_intelectual("Mimitchi","Azul")
tamagotchi_relax = tamagotchi_version_relax("Kuchipatchi","Verde")

lista_tamagotchis = [tamagotchi_tierno, tamagotchi_intelectual, tamagotchi_relax]

print(f"\n--- Bienvenido al juego de Tamagotchi! ---")
print(f"\n Registrate para poder iniciar el juego.")
    
nombre = input("\nIngresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

print("\nAhora elige tu Tamagotchi:")
for j, tamagotchi in enumerate(lista_tamagotchis):
    print(f"[{j+1}] {tamagotchi.nombre} ({tamagotchi.color})")

eleccion_str = input("Ingresa el número de tu elección: ")
if eleccion_str.isdigit():  
    eleccion = int(eleccion_str) - 1

    if eleccion < 0 or eleccion >= len(lista_tamagotchis):
        print("Elección no válida. El programa ha finalizado.")
        exit()

    tamagotchi_seleccionado = lista_tamagotchis[eleccion]
    jugador = Persona(nombre, apellido, tamagotchi_seleccionado)

    print(f"\n¡Hola, {jugador.nombre_jugador}! Has elegido a {jugador.tamagotchi.nombre}.")

    print("\n--- Estado inicial de tu Tamagotchi ---")
    print(jugador.tamagotchi)  # Usa el método __str__ para mostrar un resumen
    jugador.tamagotchi.mostrar_estado() # Muestra el emoji correspondiente

    print("\n--- El juego comienza ---")            
    

    while True:
        if jugador.tamagotchi.salud <= 0:
            print("\n¡Oh no! La salud de tu Tamagotchi ha llegado a 0.")
            jugador.tamagotchi.mostrar_estado()  # Muestra el estado final de muerte
            print("¡El juego ha terminado!")
            break 
        print("\n¿Qué deseas hacer con tu Tamagotchi?")
        print("[1] Jugar con el Tamagotchi")
        print("[2] Darle de comer")
        print("[3] Curarlo")
        print("[4] Realizar su actividad especial")
        
        if jugador.tamagotchi.tiene_caca:
             print("[5] Recoger la caca")

        print("[exit] Salir del juego")

        opcion = input("Ingresa el número de tu elección: ")

        if opcion == '1':   
                jugador.jugar_con_tamagotchi()
                
        elif opcion == '2':
                jugador.darle_comida()
                
        elif opcion == '3':  
                jugador.curarlo()       
                

        elif opcion == '4':
            if isinstance(jugador.tamagotchi, tamagotchi_version_tierno):
        # Si es el tamagotchi tierno, llamamos a su método único
                jugador.tamagotchi.oler_flores_actividad()

            elif isinstance(jugador.tamagotchi, tamagochi_version_intelectual):
            # Si es el tamagotchi intelectual, llamamos a su método único
                jugador.tamagotchi.aprender_actividad()

            elif isinstance(jugador.tamagotchi, tamagotchi_version_relax):
        # Si es el tamagotchi relax, le damos un submenú con sus 2 opciones
                print("¿Qué actividad de relax deseas hacer?")
                print("[1] Bañarse en aguas termales")
                print("[2] Pasear en el bosque")
                opcion_relax = input("Elige una opción: ")

                if opcion_relax == '1':
                    jugador.tamagotchi.bañarse_aguas_termales_actividad()
                elif opcion_relax == '2':
                    jugador.tamagotchi.pasear_bosque_actividad()
                else:
                    print("Opción no válida.")

        elif opcion == '5'and jugador.tamagotchi.tiene_caca == True:
                jugador.limpiar_caca_tamagotchi()
                
        elif opcion == 'exit' :
                print(f"¡Gracias por jugar con {jugador.tamagotchi.nombre}!")
                break  # Aquí es donde debe ir el break para salir del bucle while
        else:
            print("Opción no válida. Por favor, elige una opcion del 1 al 3.")  
        jugador.tamagotchi.mostrar_estado()

    print("\n--- El juego ha terminado ---")        