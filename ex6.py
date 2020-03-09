def degree5(n):
    if n % 5 != 0:
        return -1
    if n == -5:
        return -1
    if n == 5:
        return 1
    else:
        return degree5(n/5) + 1
