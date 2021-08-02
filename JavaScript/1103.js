const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const input = require('fs').readFileSync('./stdin', 'utf8');
const lines = input.split('\n')

// Alarme Despertador
// hh:mm (i) => hh:mm (f) = xxx minutos

const executar = (dados) => {

    const obter_minutos = () => {
        const _d = 60 * 24
        const get_i = () => dados[0] === 0 ? (dados[1] + _d) : (dados[1] + (dados[0] * 60))
        const get_f = () => dados[2] === 0 ? (dados[3] + _d) : (dados[3] + (dados[2] * 60))

        return get_f() > get_i() ? get_f() - get_i() : _d - (get_i() - get_f())
    }

    ((dados[0] + dados[1] + dados[2] + dados[3]) === 0) ? true : console.log(obter_minutos())
}

lines.forEach((e) => {
    executar(e.split(' ').map(n => Number(n)))
})

// Testes

// 1 5 3 5
// 23 59 0 34
// 21 33 21 10
// 0 0 0 0