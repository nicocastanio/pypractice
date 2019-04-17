"""
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.
"""
# Complete the plusMinus function below.
def plusMinus(arr):
    pos = neg = zer = 0
    tot = len(arr)
	
    for i in range(0, tot):
        if arr[i] > 0: 
            pos += 1
        elif arr[i] < 0: 
            neg += 1
        else: 
            zer += 1
			
    if tot > 0: 
        pos = pos / tot
        neg = neg / tot
        zer = zer / tot

    print("%8.6f"% (pos))
    print("%8.6f"% (neg))
    print("%8.6f"% (zer))
	