#Importar libreria
import random
#Opciones
contador1=int(input("cuantas rondas quieres jugar: "))
op = ("Piedra","Papel","Tijera")
contador=1
puntuacion_usuario=0
puntuacion_cpu=0
ganador=0
while ganador>=0:
    while contador<=contador1:
        #Entradas
        contador += 1
        usuario = input("Digite la opción Pierdra, Papel o Tijera:  ")
        cpu = random.choice(op)
        #Imprimir informacion
        print(f"La op que digito el usuario es: {usuario}")
        print(f"La op CPU es: {cpu}")
        #Proceso
        if usuario == "Piedra" and cpu == "Piedra":
            print("Empate!!!")
        elif usuario == "Tijera" and cpu == "Tijera":
            print("Empate!!!")
        elif usuario == "Papel" and cpu == "Papel":
            print("Empate!!!")
        elif usuario == "Piedra" and cpu == "Papel":
            print("Gana cpu!!!")
            puntuacion_cpu +=1
        elif usuario == "Piedra" and cpu == "Tijera":
            print("Gana usuario!!!")
            puntuacion_usuario +=1
        elif usuario == "Papel" and cpu == "Piedra":
            print("Gana usuario!!!")
            puntuacion_usuario +=1
        elif usuario == "Papel" and cpu == "Tijera":
            print("Gana cpu!!!")
            puntuacion_cpu +=1
        elif usuario == "Tijera" and cpu == "Piedra":
            print("Gana cpu!!!")
            puntuacion_cpu +=1
        elif usuario == "Tijera" and cpu == "Papel":
            print("Gana usuario!!!")
            puntuacion_usuario +=1

        else:
            print("Error!!!")
            contador -=1
        print(f"vas {puntuacion_usuario} puntos y la cpu va {puntuacion_cpu} puntos")

    if puntuacion_usuario>puntuacion_cpu:
        print(f"gana el usuario con {puntuacion_usuario} puntos y perdio la cpu con {puntuacion_cpu} puntos")
        break
    elif puntuacion_usuario<puntuacion_cpu:
        print(f"gana la cpu con {puntuacion_cpu} puntos y perdiste con {puntuacion_usuario} puntos")
        break
    elif puntuacion_cpu==puntuacion_usuario:
        print(f"fue un empate la cpu gano {puntuacion_cpu} y tu tuviste{puntuacion_usuario}  puntos¨")
        print("Fue un empate se vuelve a jugar :v")
        break
       
        
        