def decode(baba):
    a = len(baba)
    i = 0
    result = ''
    while i < a:
        result += str(int(baba[i]) - 3)
        i += 1
    return result