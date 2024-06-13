def rsa_decode(input, d, n):
    result = []
    for block in input:
        a = int(block)
        dec_a = pow(a, d, n)
        result.append(chr(dec_a))
    return ''.join(result)
