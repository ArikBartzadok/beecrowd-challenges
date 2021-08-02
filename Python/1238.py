def execucoes():
    return int(input())

def entradas():
    return input().split(' ')

def imprimir(v):
    print(v)

def tamanho_a(a):
    return len(a)

def tamanho_b(b):
    return len(b)

def diferenca_tamanhos(a, b):
    return (len(a) <= len(b))

def analisar(e, i, s):
    a, b = e
    if(diferenca_tamanhos(a, b)):
        for i in range(tamanho_a(a)):
            s += a[i]
            s += b[i]
        s += b[tamanho_a(a):]
    else:
        for i in range(tamanho_b(b)):
            s += a[i]
            s += b[i]
        s += a[tamanho_b(b):]
    
    return s

def combinador():
    n = execucoes()
    for i in range(n): imprimir(analisar(entradas(), i, ''))

combinador()