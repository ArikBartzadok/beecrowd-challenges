// var input = require('fs').readFileSync('./stdin', 'utf8');
var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const somar_consecutivos = (n) => {
    if (n % 2 !== 0)
        n = ++n

    let cont = 0
    let somatorio = 0

    while(cont < 5){
        cont === 0
            ? somatorio = n
            : somatorio += n

        n = n + 2
        
        cont++
    }

    console.log(somatorio)
}

// executando...
lines.forEach(e => e > 0 ? somar_consecutivos(Number(e)) : null);

// 4
// 11
// 0