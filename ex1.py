def pownum(a, n):
    if n == 1:
        return a
    else:
        return a * pownum(a, n-1)
