const Table = require('cli-table');
const prompt = require('prompt-sync')({sigint: true});

const formas_geometricas = {
    triangulo: async function () {
        const b = prompt('\n> Informe a medida da base do triângulo (isóceles): ')
        const h = prompt('\n> Informe a medida da altura do triângulo (isóceles): ')

        const area = ((b*h)/2)
        const perimetro = (b * 3)

        console.log(`> Área: ${area}, perímetro: ${perimetro}`);

        historico.push({
            figura: 'Triângulo (isóceles)',
            perimetro: perimetro,
            area: area
        }) 
    },
    circulo: async function () {
        const r = prompt('\n> Informe a medida do raio do círculo: ')

        const area = (Math.pow(r, 2) * Math.PI.toFixed(5))
        const perimetro = ((2 * Math.PI.toFixed(5)) * r)

        console.log(`> Área: ${area}, perímetro: ${perimetro}`);

        historico.push({
            figura: 'Círculo',
            perimetro: perimetro,
            area: area
        }) 
    },
    quadrado: async () => {
        const lado = prompt('\n> Informe o lado do quadrado: ')

        const area = (Math.pow(lado, 2))
        const perimetro = (lado * 4)

        console.log(`> Área: ${area}, perímetro: ${perimetro}`);

        historico.push({
            figura: 'Quadrado',
            perimetro: perimetro,
            area: area
        }) 
    },
    retangulo: async function () {
        const lado = prompt('\n> Informe a medida do lado do retângulo: ')
        const comp = prompt('\n> Informe o comprimento do retângulo: ')

        const area = (lado * comp)
        const perimetro = ((lado * 2) + (comp * 2))

        console.log(`> Área: ${area}, perímetro: ${perimetro}`);

        historico.push({
            figura: 'Retângulo',
            perimetro: perimetro,
            area: area
        }) 
    }
}

const visualizarHistorico = () => {
    console.log('-----------------------------------Histórico (DESC)------------------------------------')    

    let tabela = new Table({
        head: ['Figura', 'Área', 'Perímetro'],
        colWidths: [30, 20, 30]
    });

    historico.reverse().splice(0,5).forEach((e) => tabela.push(Object.values(e)))

    console.log(tabela.toString());
}
const encerrar = () => {
    visualizarHistorico()
    
    process.exit(0);
}

let historico = []

const iniciar = async () => {

    const calcular = async () => {
        console.log('---------------------------------------------------------------------------------')
        console.log('\n> Escolha uma das seguintes formas geométricas para calcular a área e perímetro:\n')
        Object.keys(formas_geometricas).forEach((e, i) => console.log(`> ${i + 1} - ${e}`))

        const leitor = (primeira = false) => {
            const invocador = f => ({
                '1': 'triangulo',
                '2': 'circulo',
                '3': 'quadrado',
                '4': 'retangulo'
            })[f] || 'reinvocar'

            if (!primeira) console.log('> Digite uma opção válida: ');
    
            const formula = prompt("\n> ")
    
            isNaN(formula)
                ? leitor(false)
                : formas_geometricas[invocador(formula)]()
        }

        leitor(true)

        const continuar = prompt('\n Deseja continuar calculando outras áreas? [s/n]')

        return continuar.toLowerCase() == 's'
            ? calcular()
            : encerrar()
    }
    
    calcular()
}

// vaaamo lá...
iniciar()