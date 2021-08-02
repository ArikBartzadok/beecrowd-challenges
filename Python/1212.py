def obter_entradas():
    e = input().split()
    return list(map(int, e))

def analisar_saida(x, y):
    return ((x == 0) and (y == 0))

def sem_operacoes():
    print("No carry operation.")

def exibir_operacoes(op):
    print("1 carry operation.") if (op == 1) else print("{} carry operations.".format(op))

def carry_x_menor(x, y):
    return (len(str(x)) < len(str(y)))

def carry_y_menor(x, y):
    return (len(str(y)) < len(str(x)))

def incrementar_x(x):
    return ('0' + str(x))

def incrementar_y(y):
    return ('0' + str(y))

def obter_rearanjo(x):
    return reversed(range(0, len(str(x))))

def carry_operavel(x, y, z):
    return ((int(str(x)[i]) + int(str(y)[i]) > 9) or (((int(str(x)[i]) + int(str(y)[i]) + z)) > 9))

def atualizar_carry(op, z):
    return [(op + 1), 1]

while(True):
    x, y = obter_entradas()
    op, z = [0, 0]
    
    if(analisar_saida(x, y)): break
    
    while(carry_x_menor(x, y)): x = incrementar_x(x)
    while(carry_y_menor(x, y)): y = incrementar_y(y)
    
    for i in obter_rearanjo(x):
        if (carry_operavel(x, y, z)): op, z = atualizar_carry(op, z)
        else: z = 0
    
    sem_operacoes() if (op == 0) else exibir_operacoes(op)