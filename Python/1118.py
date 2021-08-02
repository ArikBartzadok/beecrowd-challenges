def analisar_limite_execucao(ex):
    return (ex < 2)

def obter_entrada():
    e = float(input())
    return e

def nota_dentro_limite(e):
    return (e >= 0 and e <= 10)

def exibir_nota_invalida():
    print("nota invalida")

def exibir_media(acc):
    print("media = {:.2f}".format((acc/2)))

def exibir_menu():
    print("novo calculo (1-sim 2-nao)")
    op = int(input())
    return op

def analisar_opcao(op):
    return (op == 1 or op == 2)

def analisar_saida(op):
    return (op == 2)


while True:
    acc, _ex, op = [0, 0, 0]

    while (analisar_limite_execucao(_ex)):
        e = obter_entrada()
        if(nota_dentro_limite(e)):
            _ex += 1
            acc += e
        else:
            exibir_nota_invalida()
    
    exibir_media(acc)
    
    while True:
        op = exibir_menu()
        if(analisar_opcao(op)):
            break
    
    if(analisar_saida(op)):
        break