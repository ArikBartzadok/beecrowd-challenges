def execucoes():
    return int(input())

def entradas():
    return input()

def deslocamento():
    return int(input())

def imprimir(v):
    print(v)

def limite_ascii(p):
    return (p < 65)

def acsii_deslocado(c, d):
    return (ord(c)-d)

def cifrar(p, c, d, l):
    return chr(91-(65-p)) if (l) else chr(ord(c)-d)

def processar(e, d, s):
    for c in e:
        p = acsii_deslocado(c, d)

        if (limite_ascii(p)): s += cifrar(p, c, d, True)
        else: s += cifrar(p, c, d, False)

    return s

def cifra(n):
    for i in range(n): imprimir(processar(entradas(), deslocamento(), ''))

cifra(execucoes())