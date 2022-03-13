var input = require('fs').readFileSync('./stdin', 'utf8');
var lines = input.split('\n');

const [A, B] = lines.map(e => Number(e))

const SOMA = A + B

console.log(`SOMA = ${SOMA}`)