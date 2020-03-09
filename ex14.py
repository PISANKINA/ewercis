def numbers(x):
    if x == 0:
        return x
    else:
        a = x % 10
        print(a)
        return numbers(x//10)
