#CHECKPOINT_5

#Cree un bucle For de Python.
numeros = [1, 3 ,4 ,5]

for numero in numeros:
    print(numero)

#Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
def suma(a, b, c):
    return a + b + c



nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

encontrado = False
for n in lista_nombre:
    if nombre in lista_nombre:
        encontrado = True
        break

if encontrado:
    print(f"{nombre} está en la lista.")
else:
    print(f"{nombre} no está en la lista.")


resultado = suma(1, 2, 3)
print(f"La suma de 1, 2 y 3 es: {resultado}")

#Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

suma = lambda a, b, c: a + b + c

resultado = suma(1, 2, 3)
print(resultado)  


#Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista.

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

existe = False
for n in lista_nombre:
    if nombre in lista_nombre:
        existe = True
        break

if existe:
    print(f"{nombre} está en la lista.")
else:
    print(f"{nombre} no está en la lista.")




