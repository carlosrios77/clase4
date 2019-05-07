#1. suma
suma=lambda x,y:x+y
resta=lambda x,y:x-y
multiple=lambda x,y:x*y
divide=lambda x,y:x/y
import math
potencia=lambda x,y:math.pow(x,y)
raiz=lambda x,y:math.pow(x, 1/y)

x=3
y=2

lista_funciones = [suma,resta,multiple,divide,potencia,raiz]
for mi_funcion in lista_funciones:
    print('resultado=', mi_funcion(x,y))

#2. Crear un diccionario de funciones de suma y resta

calculadora = {
    'suma' : lambda x,y:x+y,
    'resta' : lambda x,y:x-y
}

#usando dic
print('usando dict')
for f in calculadora.values():
    print('resultado=', f(x,y))

pass