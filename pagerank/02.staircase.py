"""
Consider a staircase of size n=4 :

   #
  ##
 ###
####

Observe that its base and height are both equal to n, and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n .
"""

# Complete the staircase function below.
def staircase(n):
    c = "#"
    for i in range(0,n): 
        s = c*(i+1)
        print(s.rjust(n))
