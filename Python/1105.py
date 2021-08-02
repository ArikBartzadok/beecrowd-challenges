def obter_bancos_debentures():
    e = input().split()
    return list(map(int, e))

def obter_reservas_monetarias():
    e = input().split()
    return [i for i in list(map(int, e))]

def obter_bancos_credores_devedores():
    e = input().split()
    return list(map(int, e))

def imprimir(res):
    print('S' if (res == 1) else 'N')

while True:
    b, n = obter_bancos_debentures()
    
    if (all(i == 0 for i in [b, n])): break

    rm, res = [obter_reservas_monetarias(), 1]

    for i in range(n):
        d, c, v = obter_bancos_credores_devedores()
        rm[d-1] -= v
        rm[c-1] += v
    for i in rm:
        if i < 0:
            res = 0
            break
    
    imprimir(res)