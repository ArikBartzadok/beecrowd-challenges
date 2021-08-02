def obter_casos_teste():
    e = int(input())
    return e

def obter_entradas():
    e = input().split()
    return e

def analisar_ultimos_digitos(x, y):
    return (y == x[len(x)-len(y):len(x)])

def exibir_analise(res):
    print("encaixa") if res else print("nao encaixa")

t = obter_casos_teste()

for i in range(t):
    x, y = obter_entradas()

    exibir_analise(analisar_ultimos_digitos(x, y))