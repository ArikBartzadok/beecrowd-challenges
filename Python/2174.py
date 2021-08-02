def quantidade():
    return int(input())

def pokemon():
    return input()

def imprimir(v):
    return print('Falta(m) {:.0f} pomekon(s).'.format(v))

def calcular(l):
    return (151 - len(l))

def processar(n, l):
    for _ in range(n):
        p = pokemon()
        if p not in l: l.append(p)
    
    return l

def pokebola():
    imprimir(calcular(processar(quantidade(), [])))
    
pokebola()