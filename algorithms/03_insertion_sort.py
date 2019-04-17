"""
Insertion Sort
"""
from random import randint
from time import time


lista = []
for i in range(0,10000):
    lista.append(randint(0,1000000))    # agrega nro aleatorio entre 0 y 1000000

#print(lista)
tiempo_inicial = time()

for i in range(0, len(lista)):
    valor = lista[i]
    j = i-1
    while j>=0 and valor < lista[j]:
        lista[j+1] = lista[j]
        j = j-1
    lista[j+1] = valor

tiempo_final = time()
#print(lista)

print("Tiempo ejecución: "+str(tiempo_final - tiempo_inicial))
