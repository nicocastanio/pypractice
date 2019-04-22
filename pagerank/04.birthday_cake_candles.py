"""
Birthday Cake Candles

You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age.
When she blows out the candles, she’ll only be able to blow out the tallest ones.
Your task is to find out how many candles she can successfully blow out.
"""

#
def birthdayCakeCandles(ar):
    cont = 0
    mayor = ar[0]
    for i in range(0,len(ar)):
        if ar[i] > mayor:
            mayor = ar[i]
            cont = 1
        elif ar[i] == mayor:
            cont += 1
    return cont

