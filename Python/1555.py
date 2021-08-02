import math

def obter_casos_teste():
    e = int(input())
    return e

def verificar_execucao(t):
    return (t > 0)

def obter_entradas():
    e = input().split()
    return list(map(int, e))

def calcula_rafa(x, y):
    return (math.pow((3 * x), 2) + math.pow(y, 2))

def calcula_beto(x, y):
    return ((2 * (math.pow(x,2))) + math.pow((5 * y), 2))

def calcula_carlos(x, y):
    return ((-100 * x) + (math.pow(y, 3)))

def realizar_calculos(x, y):
    r = calcula_rafa(x, y)
    b = calcula_beto(x, y)
    c = calcula_carlos(x, y)

    exibir_resultado(r, b, c)

def exibir_resultado(r, b, c):
    print("Rafael ganhou") if (r > b and r > c) else (print("Beto ganhou") if (b > r and b > c) else print("Carlos ganhou"))

def decrementar_execucao(t):
    return (t - 1)

t = obter_casos_teste()

while verificar_execucao(t):
    x, y = obter_entradas()
    
    realizar_calculos(x, y)

    t = decrementar_execucao(t)
