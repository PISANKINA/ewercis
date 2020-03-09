def function1(x):
    return puma(x)


def puma(x, a=2):
    if a > x**0.5:
        return 1
    elif x % a == 0:
        return 0
    else:
        return puma(x, a+1)
