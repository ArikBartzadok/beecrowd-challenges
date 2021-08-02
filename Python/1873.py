def execucoes():
    return int(input())

def entradas():
    return input().split()

def imprimir(v):
    print(v)

def armas():
    return ['tesoura','pedra','spock','papel','lagarto']

def analisar(x, n):
    while (n[2] != x):
        n = ([n[-1]] + n[:-1])  

    return n

def extrair(z, y):
    return 2-z.index(y)

def processar():
    x, y = entradas()  
    r = extrair(analisar(x, armas()), y)

    return 'rajesh' if(r > 0) else ('sheldon' if (r < 0) else 'empate')

def jogo(n):
    while True:
        n -= 1
        imprimir(processar())

        if (n <= 0): break

jogo(execucoes())