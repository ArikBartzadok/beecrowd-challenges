def entrada():
    return input()

def imprimir(v):
    print(v)

def caractere_espaco(c):
    return c == ' '

def trocar_caixa(c):
    return (not c)

def processar(e, s, m):
    for l in e:
        if caractere_espaco(l):
            s += ' '
            continue
        if m:
            s += l.upper()
            m = trocar_caixa(m)
        else:
            s += l.lower()
            m = trocar_caixa(m)
    
    return s

def seq_dancante():
    while True:
        try:
            imprimir(processar(entrada(), '', True))
        except EOFError:
            break

seq_dancante()