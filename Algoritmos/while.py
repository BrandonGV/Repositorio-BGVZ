#Variable
"""""
contador = 0

#Estructura
while contador <= 4:
    if contador == 3:
        print("unisangil")
        break
    print(f"contador = {contador}")
    contador += 1
print("salio del while")

#Break y continue
#Ejemplo
contador= 0
while contador<20:
    contador += 1
    if contador<15:
        continue
    print(contador)
"""""
texto="Estoy en clase de algoritmos en unisangil"
#Buscar
print( "clase" in texto )
print(texto.title())#titulo
print(texto.upper())#Mayuscular
print(texto.lower())#Minusculas
print(texto.count("a"))#contar

