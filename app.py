

import random


print("Juego piedra, papel o tijera")
print("Comencemos a jugar : ")

#read integer form console


opcion = input("Elija una opcion entre 1- piedra, 2- papel, 3- tijera: ")
#read input integer from console



seguir = 'S'

def printOpcion(opcion, quiensoy):
    soy = "Maquina eligió "
    if(quiensoy == 1):
        soy = "Usted eligió "

    if opcion == "1":
        print(soy + " piedra")
    elif opcion == "2":
        print(soy + " papel")
    elif opcion == "3":
        print(soy + " tijera")
    else:
        print("Opcion incorrecta")

def printWinner(opcion, opcionMaquina):
    if opcion == "1" and opcionMaquina == "3":
        print("Usted ganó")
    elif opcion == "2" and opcionMaquina == "1":
        print("Usted ganó")
    elif opcion == "3" and opcionMaquina == "2":
        print("Usted ganó")
    elif opcion == opcionMaquina:
        print("Empate")
    else:
        print("Usted perdió")

while seguir == 'S' :
        printOpcion(opcion, 1)
        opcionMaquina = random.randint(1,3)
        printOpcion(str(opcionMaquina), 2)
        printWinner(opcion, str(opcionMaquina))
        seguir = input("Desea seguir jugando? S/N: ")n
        if seguir == 'S' or seguir == 's':
            opcion = input("Elija una opcion entre 1- piedra, 2- papel, 3- tijera: ")
            seguir = 'S'
    



