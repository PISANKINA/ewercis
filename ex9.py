def factorial(n):
    b = 1
    for i in range(2, n+1):
        b *= i
    return b


def combin(n, k):
    c = factorial(n)//(factorial(k)*factorial(n-k))
    return c
