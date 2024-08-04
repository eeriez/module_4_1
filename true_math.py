from math import inf

def divide (first, second):
    first = int(first)
    second = int(second)

    if second == 0:
        return inf
    else:
        return first/second
