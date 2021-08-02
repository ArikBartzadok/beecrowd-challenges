var input = require('fs').readFileSync('./stdin', 'utf8');
var lines = input.split('\n');

const [A, B] = lines.map(e => Number(e));

const MEDIA_PONDERADA = ((A * 3.5) + (B * 7.5))/(11);

console.log(`MEDIA = ${MEDIA_PONDERADA.toFixed(5)}`);