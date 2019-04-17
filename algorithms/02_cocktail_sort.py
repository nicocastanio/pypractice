"""
Método de ordenamiento - Cocktail Sort
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
    # print(lista)
    #
    for k in range(len(lista-j), j, -1):
        if lista[k] > lista[k-1]:
            temp = lista[k]
            lista[k] = lista[k-1]
            lista[k-1] = temp

print(lista)

