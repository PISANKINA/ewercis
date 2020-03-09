def odd_list(a, n):
    if n == 0:
        return []
    number = a[-n]
    if number % 2 > 0:
        return odd_list(a, n-1)
    else:
        return [number] + odd_list(a, n-1)
