def obter_casos_teste():
    e = int(input())
    return e

def obter_entradas():
    e = input().split()
    return list(map(int, e))

def verificar_execucao(t):
    return (t > 0)

def exibir_resultado(x, y):
    print("{:.0f} cm2".format(((x*y)/2)))

def decrementar_execucao(t):
    return (t - 1)

t = obter_casos_teste()

while verificar_execucao(t):
    x, y = obter_entradas()

    exibir_resultado(x, y)
    
    t = decrementar_execucao(t)
