def quantidade():
    return int(input())

def entradas():
    return input().split()

def imprimir(v):
    print(v)

def dicionario(i):
    return ['URI', 'OBI'][i]

def analise_inicio(_i, v):
    return (_i[0:2]==v) and (len(_i)==3)

def analisar(p):
    for i, _i in enumerate(p):
        if(analise_inicio(_i, 'UR')): p[i] = dicionario(0)
        if(analise_inicio(_i, 'OB')): p[i] = dicionario(1)
            
    return (' '.join(p))

def corrigir(n, p):
    imprimir(analisar(p))

corrigir(quantidade(), entradas())