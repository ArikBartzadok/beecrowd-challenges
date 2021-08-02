import math

def ordem_matricial(mx):
    return int(math.sqrt(len(mx)))

def somar(mx):
    ex, ro, cs, sm = [0, 1, 1, 0]

    def processar():
        nonlocal ex, ro, cs, sm
        
        ex += 1
        x = mx[cs]

        if(ex == (ordem_matricial(mx) - ro)): cs += ro + 1
            
        if(ex == (ordem_matricial(mx) - ro)): ex = 0
        else: ex = ex

        if(ex == (ordem_matricial(mx) - ro)):ro += 1
        else:ro = ro

        cs += 1
        sm += x
        
        analisar()
    
    def analisar():
        imprimir(sm) if (ro == ordem_matricial(mx)) else processar()

    analisar()

def media(mx):
    print()

def imprimir(v):
    print('{:.1f}'.format(v))

def obter_entradas():
    o, mx = [input(), []]
    for i in range(25): mx.append(float(input()))
    
    return o, mx

def executar():
    o, mx = obter_entradas()
    somar(mx) if (o == 'S') else media(mx)

executar()