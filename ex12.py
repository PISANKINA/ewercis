def search(a, x):
    if len(a) == 0:
        return 0
    if a[-1] == x:
        return 1
    else:
        return search(a[:-1], x)
