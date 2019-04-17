"""
Método de ordenamiento - Burbuja o Bubble Sort
"""

lista = [20,15,8,23,87,1]

print(lista)

temp = 0

for j in range(1,len(lista)):
    for i in range(0,len(lista)-j):
        if lista[i] > lista[i+1]:
            temp = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = temp
    print(lista)

print(lista)

