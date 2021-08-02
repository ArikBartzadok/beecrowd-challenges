def obter_entradas():
    e = input().split(' ')
    return e

def executar(dados):
    return obter_minutos(dados)

def obter_minutos(dados):
    _d = 60 * 24
    _i = get_i(dados, _d)
    _f = get_f(dados, _d)

    return _f - _i if (_f > _i) else _d - (_i - _f)

def get_i(dados, _d):
    return (dados[1] + _d) if (dados[0] == 0) else (dados[1] + (dados[0] * 60))

def get_f(dados, _d):
    return (dados[3] + _d) if (dados[2] == 0) else (dados[3] + (dados[2] * 60))

while True:
    dados = list(map(int, obter_entradas()))
    
    if((dados[0] + dados[1] + dados[2] + dados[3]) == 0):
        break
    else:
        print(executar(dados))
