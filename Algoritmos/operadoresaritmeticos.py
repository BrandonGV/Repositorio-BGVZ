
#libreria

import math
#PRIMER EJERCICIO
operador = ((15/3)*(7+(68-15*33+((45**2)/5)/3)/2)+19)
print(float(operador))
#SEGUNDO EJERCICIO

operador2 = (4+8*2)/4-3**2+math.sqrt(4)
print(float(operador2))
#addiquirir informacion
a = int (input("digite el numero 1:"))
print(f"el numero a es:{a}")
b = int (input("digite el numero 2:"))
print(f"el numero a es:{b}")

#proceso
c = a + b
d = a - b
e = a * b
f = a / b
g = a ** b
h = math.sqrt(a)

#salida
print(f"el resultado de la suma es : {c}")
print(f"el resultado de la resta es : {d}")
print(f"el resultado de la multiplicación es : {e}")
print(f"el resultado de la división es : {f}")
print(f"el resultado de la potencia es : {g}")
print(f"el resultado de la raiz de a es : {h}")
