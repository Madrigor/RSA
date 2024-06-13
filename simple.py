def simpleNum(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True
