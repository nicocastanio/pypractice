"""
Insertion Sort
"""
from random import randint
from time import time


#lista = [15,63,34,88,10]
lista = []
for i in range(0,10000):
    lista.append(randint(0,1000000))    # agrega nro aleatorio entre 0 y 1000000

#print(lista)
tiempo_inicial = time()

"""
# opcion 1 
for i in range(0, len(lista)):
    minimo = lista[i]
    for j in range(i, len(lista)):
        if lista[j] < minimo:
            lista[i] = lista[j]
            lista[j] = minimo 
            minimo = lista[i]
"""
# opcion 2             
for i in range(0, len(lista)-1):
    minimo = i
    for j in range(i+1,len(lista)):
        if lista[j] < lista[minimo]:
            minimo =  j
    aux = lista[minimo]
    lista[minimo] = lista[i]
    lista[i] = aux
    

tiempo_final = time()
#print(lista)

print("Tiempo ejecución: "+str(tiempo_final - tiempo_inicial))
