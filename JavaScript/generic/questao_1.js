const calcular_fatorial = x => [0, 1].includes(x)
    ? 1
    : x * calcular_fatorial(x - 1)

console.log(calcular_fatorial(3)) // 6