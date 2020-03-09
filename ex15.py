def destrobin(x):
    return binary(x)


def binary(x, a=''):
    if x == 0:
        return a
    else:
        return binary(x//2, str(x % 2) + a)
