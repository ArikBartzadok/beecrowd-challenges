const retorna_raiz = (a, b, c) => {
    const delta = () => ((b*b) - (4 * a * c))

    const raiz_one = () => ((b * -1) + Math.sqrt(delta()))/(2 * a)

    const raiz_two = () => ((b * -1) - Math.sqrt(delta()))/(2 * a)

    return ` O x1 vale: ${raiz_one()}, e o x2 vale: ${raiz_two()}`
}

console.log(retorna_raiz(2, 8, -24)) // 2, -6