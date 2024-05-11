#Lista
lista = ["sony","sega","nintendo","google","microsoft"]

#Tupla:
tupla = (1,2,3,4,5)

#Flotante
flotante = 7.65

#Entero
entero = 78

#Decimal
from decimal import Decimal
decimal = Decimal('8.545465')

#Diccionario
diccionario = {
    "color" : "rojo",
    "ciudad": "Barcelona",
    "deporte": "futbol",
}

print(lista)
print(tupla)
print(flotante)
print(entero)
print(decimal)
print(diccionario)

import math
flotante_redondeado = math.ceil(flotante)
raiz_cuadrada = math.sqrt(flotante)
primer_elem = diccionario["color"]
segundo_elem = tupla[1]
nueva_lista = lista + ['yahoo']
remplazado = "asus"
lista[0] = remplazado
tupla = tupla + (6,)



print("ejercicio 2:",flotante_redondeado)
print("ejercicio 3:", flotante, "es:", raiz_cuadrada)
print("ejercicio 4:",primer_elem)
print("ejercicio 5:", segundo_elem)
print("ejercicio 6:",nueva_lista)
print("ejercicio 7:", lista)
lista.sort()
print("ejercicio 8:", lista)
print("ejercicio 9:", tupla)
