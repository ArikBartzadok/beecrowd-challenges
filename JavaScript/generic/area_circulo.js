var input = require('fs').readFileSync('./stdin', 'utf8');
var lines = input.split('\n');

const [R] = lines.map(e => Number(e));

const AREA = Math.pow(R, 2) * Math.PI.toFixed(5);

console.log(`A=${AREA.toFixed(4)}`);