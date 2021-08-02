var input = require('fs').readFileSync('./stdin', 'utf8');
var lines = input.split('\n');

const [A, B, C] = lines.map(x => x.split(" ").map(y => Number(y))).flat();

const TRIANGULO = (b, h) => ((b*h)/2);
const CIRCULO = r => (Math.pow(r, 2) * Math.PI.toFixed(5));
const TRAPEZIO = (bma, bme, h) => (((bma + bme) * h)/2);
const QUADRADO = l => (Math.pow(l, 2));
const RETANGULO = (c, l) => (c * l);

console.log(`TRIANGULO: ${TRIANGULO(A, C).toFixed(3)}`);
console.log(`CIRCULO: ${CIRCULO(C).toFixed(3)}`);
console.log(`TRAPEZIO: ${TRAPEZIO(A, B, C).toFixed(3)}`);
console.log(`QUADRADO: ${QUADRADO(B).toFixed(3)}`);
console.log(`RETANGULO: ${RETANGULO(A, B).toFixed(3)}`);