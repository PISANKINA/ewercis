def sum_progress(a1, r, n):
    if n == 1:
        return a1
    else:
        return sum_progress(a1 + r, r, n-1) + 1
