#Estructura
import random
"""
for control in range(0,10,2):
    print(control)

#listas
lista = [1,2,3,True,"unisangil",3.44]
tupla =(1,2,34,5)
print(lista[3])
print(lista[:])
print(lista[3:])
print(lista[:3])
print(lista[3:5])
print(len(lista))

#Metodos para las listas
for control in lista:
    print(control)
for control in tupla:
    print(control)  
#insert
print(lista.insert(3,"u"))
print(lista)
#append
lista.append(123)
print(lista)
#pop
lista.pop()
print(lista)
#remove
lista.remove("unisangil")
print(lista)  
"""""
#lista de 100 datos
lista_aleatoria =[random.randint(1,100) for i in range(100)]
print(lista_aleatoria)