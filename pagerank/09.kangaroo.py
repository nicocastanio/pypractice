"""
Kangaroo
"""

# It should return YES if they reach the same position at the same time, or NO if they don't.
# same time = same number of jumps
def kangaroo(x1, v1, x2, v2):
    """
    x1, v1: integers, starting position and jump distance for kangaroo 1
    x2, v2: integers, starting position and jump distance for kangaroo 2
    """
    if x1+v1 == x2+v2:
        return "YES"

    elif (x2>x1 and v2>v1) or (x2==x1 and v2>v1) or (x2>x1 and v2==v1) or (x1+v1>x2+v2 and v1>v2):
        return "NO"

    else:
        ini2 = x2 - x1
        ini1 = 0
        # this is not the best choice, for large numbers can fail
        for i in range(1,100000):
            pos1 = ini1+v1*i
            pos2 = ini2+v2*i
            if (pos1 == pos2):
                return "YES"
        return "NO"
