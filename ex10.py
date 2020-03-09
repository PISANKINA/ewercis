def maxlist(a):
    if len(a) == 1:
        return a[0]
    else:
        return max(a[0], maxlist(a[1:]))
