def count(a,b):
    if a == b:
        return 1
    else:
        if a > b:
            return 1 + count(a-b, b)
        else:
            return 1 + count(a, b-a)
