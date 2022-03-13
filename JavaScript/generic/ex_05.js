const Table = require('cli-table')
const prompt = require('prompt-sync')({sigint: true})

const iniciar = () => {
    let registros = []
    const encerrar = () => process.exit(0)
    const registrar_quantitade = () => {
        const quantidade_alunos = prompt('\n>> Informe a quantidade de alunos na turma: ')
        registrar_aluno(Number(quantidade_alunos))
    }
    const ordenar = {
        alfabetica: () => {
            registros = registros.sort((a, b) => {
                if (a.nome > b.nome)
                    return 1

                if (a.nome < b.nome)
                    return -1
                return 0
            })

            return registros
        },
        crescente: () => {
            registros = registros.sort((a, b) => {
                if (a.nota > b.nota)
                    return 1

                if (a.nota < b.nota)
                    return -1
                return 0
            })

            return registros
        },
        decrescente: () => {
            registros = registros.sort((a, b) => {
                if (a.nota > b.nota)
                    return -1

                if (a.nota < b.nota)
                    return 1
                return 0
            })

            return registros
        }
    }
    const exibir = p => {
        let tabela = new Table({
            head: ['índice', 'Nome', 'Nota'],
            colWidths: [10, 30, 20]
        });
    
        p.forEach((e, i) => tabela.push([(i + 1), ...Object.values(e)]))
    
        console.log(tabela.toString())
    }
    const escolher_exibicao = () => {
        const lista_formas = ['Alfabética', 'Crescente (nota)', 'Decrescente (nota)']
        const get_formas = f => ({
            '1': 'alfabetica',
            '2': 'crescente',
            '3': 'decrescente'
        })[f]
        console.log('\n Escolha uma forma de exibição: ')
        lista_formas.forEach((e, i) => console.log(`${i + 1} - ${e}`))
        
        const forma = prompt('\n>> ')

        exibir(ordenar[get_formas(forma)]())
    }
    const registrar_aluno = (total, atual = 1) => {
        const nome = prompt(`\n>> Informe o nome do aluno ${atual}: `)
        const nota = prompt(`\n>> Informe a nota do aluno ${atual}: `)

        registros.push({
            nome: nome,
            nota: Number(nota)
        })
        
        atual < total
            ? registrar_aluno(total, (atual + 1))
            : escolher_exibicao()
    }
    const editar = () => {
        console.log('\n>> Qual o índice do registro que deseja editar?')
        const indice = prompt('\n>> ')

        const nome = prompt('\n>> Informe o novo nome do aluno: ')
        const nota = prompt('\n>> Informe a nova nota do aluno: ')

        registros[(indice - 1)].nome = nome
        registros[(indice - 1)].nota = Number(nota)

        escolher_exibicao()

        tomar_decisao()
    }
    const tomar_decisao = () => {
        const lista_opcoes = ['encerrar', 'editar registro']
        
        console.log('\n>> Deseja encerrar ou editar algum registro?')
        lista_opcoes.forEach((e, i) => console.log(`${i + 1} - ${e}`))
        const decisao = prompt('\n>> ')

        switch(decisao){
            case '1':
                encerrar()
                break
            case '2':
                editar()
                break
            default:
                console.log('\n>> Por favor, escolha uma opção válida: ')
                tomar_decisao()
                break
        }
    }

    // cadastrando...
    registrar_quantitade()

    tomar_decisao()
}

iniciar()