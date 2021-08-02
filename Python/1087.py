def obter_entradas():
    e = input().split(" ")
    return list(map(int, e))

def analisar_parada(x1, y1, x2, y2):
    return ((x1 + y1 + x2 + y2) == 0)

def analisar_dupla_coordenada(x1, y1, x2, y2):
    return ((x1==x2) and (y1==y2))

def analisar_coordenada_singular(x1, y1, x2, y2):
    return ((x1==x2) or (y1==y2))

def analisar_diferenca_coordenadas(x1, y1, x2, y2):
    return (abs(x1-x2) == abs(y1-y2))

while True:
    x1, y1, x2, y2 = obter_entradas()

    if analisar_parada(x1, y1, x2, y2): break
    
    if analisar_dupla_coordenada(x1, y1, x2, y2):
        print(0)
        continue
    
    if analisar_coordenada_singular(x1, y1, x2, y2):
        print(1)
        continue
    
    if analisar_diferenca_coordenadas(x1, y1, x2, y2):
        print(1)
        continue
    
    print(2)