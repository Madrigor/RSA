def encry(text, p, q):
    n = p * q
    m = (p - 1) * (q - 1)
    d = Calculate_d(m)
    e = Calculate_e(d, m)
    print(f"Ваш открытый ключ: e = {e}, n = {n} ")
    print(f"Ваш закрытый ключ: d = {d}, n = {n} ")
    result = RSA_encrypt(text, e, n)
    return result


def Calculate_d(m):
    def GCD(a, b):
        while b:
            a, b = b, a % b
        return a
    d = 2
    while GCD(m, d) != 1:
        d += 1
    return d


def Calculate_e(d, m):
    e = 1
    while True:
        if (e * d) % m == 1:
            break
        else:
            e += 1
    return e


def RSA_encrypt(text, e, n):
    result = []
    for char in text:
        a = ord(char)
        enc_a = pow(a, e, n)
        result.append(str(enc_a))
    return result
