def fib(k):
    if k == 1:
        return 1
    if k == 2:
        return 1
    else:
        return fib(k-1) + fib(k-2)
