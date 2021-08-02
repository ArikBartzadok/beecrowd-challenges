def obter_entrada():
    return input()

def saida(v):
    print(v)

def processar_palavra(e):
    if(len(e)>3): saida(3)
    else:
        n = 0
        if (e[0:1]=='o'): n += 1
        if (e[1:2]=='n'): n += 1
        if (e[2:3]=='e'): n += 1

        saida(1) if(n>=2) else saida(2)

def palavra():
    n = int(obter_entrada())
    for i in range(n): processar_palavra(obter_entrada())

palavra()