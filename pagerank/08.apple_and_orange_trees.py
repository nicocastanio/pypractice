"""
Apple and Orange
"""


def countApplesAndOranges(s, t, a, b, apples, oranges):
    tota = toto = 0
    for m in apples:   # range(0, len(apples)):
        if a+m >= s and a+m <= t:
            tota += 1
    for n in oranges:
        if b+n >= s and b+n<=t:
            toto += 1

    print(tota)
    print(toto)
