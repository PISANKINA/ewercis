def ind_maxlist(a, n):
    if not n - 1:
        return 0
    if a[ind_maxlist(a, n - 1)] < a[n-1]:
        return n-1
    else:
        return ind_maxlist(a, n - 1)
