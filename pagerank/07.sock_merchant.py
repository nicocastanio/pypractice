"""
Sock Merchant
"""


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    medias = dict()  # or   medias = {}
    total = 0
    aux = 0

    # recorrer lista y armo un Dictionary con los nros (medias) para poder contarlos
    for m in ar:
        if m not in medias:
            medias[m] = 1
        else:
            medias[m] += 1
        # otra manera de hacer esto es:
        # medias[m] = medias.get(m, 0) + 1
        # en este caso no utilizamos un IF para chequear si la key existe

    # rocorro lo que conte por cada media, divido por 2 y me quedo con parte entera (pares completos) para acumular
    for i in medias:
        aux = medias[i] // 2
        total += aux
    return total
