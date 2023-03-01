precio = 500
"""""
#0 comparación
print(precio > 500) #f
print(precio >= 500) #v
print(precio < 500) #f
print(precio <= 500) #v
print(precio == 500) #v
print(precio != 500) #f
"""""
#compuertas logicas
#AND
print(False and False) #0
print(False and True) #0
print(True and False) #0
print(True and True) #1
print("-------------------AND-----------")
#NAND
print(not(False and False)) #1
print(not(False and True)) #1
print(not(True and False)) #1
print(not(True and True)) #0
print("-------------------NAND-----------")
#OR
print(False or False) #0
print(False or True) #1
print(True or False) #1
print(True or True) #1
print("-------------------OR-----------")
#NOR
print(not(False or False)) #1
print(not(False or True)) #0
print(not(True or False)) #0
print(not(True or True)) #0
print("-------------------NOR-----------")
#NOT
print(not(False)) #1
print(not(True)) #0
print("-------------------NOT-----------")

