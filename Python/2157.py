def execucoes():
    return int(input())

def entradas():
    return map(int, input().split())

def imprimir(v):
    print(v)

def inverter(v):
    return v[::-1]

def calcular(x, y, r):
    for i in range(x, (y+1)): r += str(i)
    r += inverter(r)

    return r

def processar(e):
    x, y = e

    return calcular(x, y, '')

def sequencia(n):
    for _ in range(n): imprimir(processar(entradas()))

sequencia(execucoes())