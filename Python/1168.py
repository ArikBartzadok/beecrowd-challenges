def obter_entrada():
    return input()

def obter_configs():
    #       0,1,2,3,4,5,6,7,8,9
    return [6,2,5,5,4,5,6,3,7,6]

def processar_digito(v):
    t = 0
    for i in v: t += obter_configs()[int(i)]
    saida(t)

def saida(t):
    print("{:.0f} leds".format(t))

def leds():
    n = int(obter_entrada())
    for i in range(n): processar_digito(obter_entrada())
        
leds()