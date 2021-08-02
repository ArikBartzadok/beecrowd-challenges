def execucoes():
    return int(input())

def entradas():
    return list(map(str, input().split()))

def imprimir(v):
    print(v)

def processar(e, s):
    for i in range(len(e)): s += (e[i][0])
    return s

def mensagem(n):
    for i in range(n): imprimir(processar(entradas(), ''))

mensagem(execucoes())