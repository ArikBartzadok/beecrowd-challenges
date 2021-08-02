var input = require('fs').readFileSync('./stdin', 'utf8');
var lines = input.split('\n');

const [A, B] = lines.map(e => Number(e))

const PROD = A * B

console.log(`PROD = ${PROD}`)