"""
Counting Valleys
D: downhill
U: uphill

A mountain is a sequence of consecutive steps above sea level,
starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level,
starting with a step down from sea level and ending with a step up to sea level.
"""

#
def countingValleys(n, s):
    """ n: the number of steps Gary takes
    s: a string describing his path
    """
    conta = 0
    nivel = 0
    for i in s:
        if i == 'D':
            if nivel == 0:
                conta += 1
            nivel -= 1
        elif i == 'U':
            nivel += 1
