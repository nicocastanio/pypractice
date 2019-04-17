"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

For example,  arr[1,3,5,7,9]. Our minimum sum is 1+3+5+7=16 and our maximum sum is 3+5+7+9=24. 
We would print : 
> 16 24 

"""

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minimo = maximo = 0
    arr.sort()

    # option 1
    minimo = sum(arr[0:4])
    maximo = sum(arr[-4:])
    # option 2
    #for i in range(0,len(arr)-1):
    #    minimo += arr[i]
    #for j in range(len(arr)-1, 0, -1): 
    #    maximo += arr[j]

    # output
    print(minimo, maximo)
    