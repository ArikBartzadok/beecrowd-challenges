var input = require('fs').readFileSync('./stdin', 'utf8');
var lines = input.split('\n');

// 1
// 4
// 105
// 1260

const resolver = entradas => {
    [...entradas].forEach(e => {
        console.log(e)
    })
}

// [...lines].forEach(e => resolver(e))
resolver('Rr')