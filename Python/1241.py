def execucoes():
    return int(input())

def entradas():
    return input().split()

def imprimir(v):
    print('encaixa' if (v) else 'nao encaixa')

def diferenca_tamanhos(a, b):
    return (len(a) < len(b))

def verificar_contencao(a, b):
    return (a[len(a)-len(b)::] == b)

def analisar(n):
    a, b = entradas()
    if(diferenca_tamanhos(a, b)): imprimir(False)
    else: imprimir(True) if (verificar_contencao(a, b)) else imprimir(False)
            
    n -= 1
    if (n > 0): analisar(n)

def verificar_encaixa():
    analisar(execucoes())

verificar_encaixa()