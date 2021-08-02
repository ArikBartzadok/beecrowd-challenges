def obter_entrada():
    return input()

def saida(v):
    print(v)

def array_comprimido(a):
    return ''.join(map(str, a))

def inverter_array(a):
    return a[::-1]

def formatacao_indice(l, i):
    return (l[i].isupper() or l[i].islower())

def tamanho_minimo(i, e):
    return i >= (len(e)//2)

def obter_unicode(l, i, n):
    return chr(ord(l[i]) + n) if (n == 3) else chr(ord(l[i]) - n)

def analisar_entrada(e):
    l = list(e)

    for i in range(len(e)):
        if formatacao_indice(l, i): l[i] = obter_unicode(l, i, 3)

    l = inverter_array(l)

    for i in range(len(e)):
        if tamanho_minimo(i, e): l[i] = obter_unicode(l, i, 1)

    return array_comprimido(l)

def encriptar():
    n = int(obter_entrada())
    for i in range(n): saida(analisar_entrada(obter_entrada()))

encriptar()