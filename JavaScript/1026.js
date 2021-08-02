// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const input = require('fs').readFileSync('./stdin', 'utf8');
const lines = input.split('\n')

// XOR - bit
const obter_bit_a_bit = (n) => console.log(n[0] ^ n[1])

lines.forEach((e) => obter_bit_a_bit(e.split(' ').map((n) => Number(n))))

// Teste

// 4 6
// 6 9