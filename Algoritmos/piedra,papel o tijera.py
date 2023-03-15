#Importar libreria
import random
from time import time
#Opciones
tiempo_inicial = time()
op = ("Piedra","Papel","Tijera")
contador=0
puntuacion_usuario=0
puntuacion_cpu=0
contador1=int(input("cuantas rondas quieres jugar: "))
while True:
     #Entradas
        print("*"*20)
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
        print("*"*20)
        print(f"Vas {puntuacion_usuario} puntos ")
        print(f"la cpu va {puntuacion_cpu} puntos")
        print(f"Ronda {contador}")
        print("*"*20)
        if contador==contador1:
            print(f"El resultado final fue la cpu con {puntuacion_cpu} puntos y el usuario tuvo {puntuacion_usuario} puntos")
            tiempo_final = time()
            tiempo_total = tiempo_final - tiempo_inicial
            print("ESTE PROGRAMA SE EJECUTO EN:")
            print(tiempo_total*1000) 
            print("MILISEGUNDOS")
            break
"""""
    if puntuacion_usuario>puntuacion_cpu:
        print(f"gana el usuario con {puntuacion_usuario} puntos y perdio la cpu con {puntuacion_cpu} puntos")
        break
    elif puntuacion_usuario<puntuacion_cpu:
        print(f"gana la cpu con {puntuacion_cpu} puntos y perdiste con {puntuacion_usuario} puntos")
        break
    elif puntuacion_cpu==puntuacion_usuario:
        print(f"fue un empate la cpu gano {puntuacion_cpu} y tu tuviste{puntuacion_usuario}  puntos¨")
        print("Fue un empate se vuelve a jugar :v")
        ganador +=1
"""
        
       
        
        