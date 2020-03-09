def nod(a, b):
    if a * b == 0:
        return a+b
    if a > b:
        return nod(a-b, b)
    else:
        return nod(a, b-a)
