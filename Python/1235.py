def execucoes():
    return int(input())

def entrada():
    return input()

def imprimir(v):
    print(v)

def dividir(s):
    return (int(len(s)/2) -1)

def processar(e, s):
    return (s[e::-1] + s[len(s)-1:e:-1])

def decifrar(n, e):
    n -= 1
    imprimir(processar(dividir(e), e))

    if (n > 0): decifrar(n, entrada())

decifrar(execucoes(), entrada())