const prompt = require('prompt-sync')({sigint: true});

const encerrar = (acumulado) => {
    console.log('>> Valor acumulado das operações: ', acumulado)
    process.exit(0)
}

// Sempre realizando operações sobre os resultados anteriores, exceto quando esta for a inicial
const calculadora = () => {
    console.log('\n>> Calculadora 3000....\n');
    const operar = {
        soma: (n1, n2) => (n1 + n2),
        subtracao: (n1, n2) => (n1 - n2),
        multiplicacao: (n1, n2) => (n1 * n2),
        divisao: (n1, n2) => (n1 / n2),
        fatorial: (n1) => [0, 1].includes(n1) ? 1 : n1 * operar.fatorial(n1 - 1),
        potencia: (n1, p) => (Math.pow(n1, p))
    }
    const leitor = (inicial = false, acc = 0) => {
        let n1, n2, op, res
        const lista_operadores = ['+', '-', '*', '/', '!', '^']
        const get_operador = op => ({
            '+': 'soma',
            '-': 'subtracao',
            '*': 'multiplicacao',
            '/': 'divisao',
            '!': 'fatorial',
            '^': 'potencia'
        })[op]

        const obter_n1 = () => n1 = Number(prompt('\n>> valor 1: '))
        const obter_n2 = () => n2 = Number(prompt('\n>> valor 2: '))
        const obter_operador = () => {
            console.log('\n>> Qual operação deseja realizar?')
            lista_operadores.forEach((e, i) => console.log(`( ${e} )`))
            op = prompt('\n> ')
        }
        const obter_resultado = () => res = operar[get_operador(op)](inicial ? n1 : acc, inicial ? n2 : n1)

        inicial
            ? obter_n1()
            : obter_operador()
        
        inicial
            ? obter_operador()
            : obter_n1()

        if (!['!'].includes(op)) inicial
            ? obter_n2()
            : obter_resultado()

        if (inicial) obter_resultado()

        console.log('>> Resultado: ', res)

        const decisao = prompt('\n>> Deseja continuar operando? [s/n]\n>>')

        decisao.toLowerCase() == 's'
            ? leitor(false, res)
            : encerrar(res)
    }

    leitor(true)
}

calculadora()