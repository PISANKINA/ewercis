def simmetr(s,i,j):
    if len(s) == 1:
        return True
    s[i] = s[0]
    if s[i] == s[j]:
        return True
    else:
        return s[i] == s[j] and simmetr(s[1:-1], i, j)
