const imprime_matrix = n => {
    var saida = '';

    let exec = 0
    let numexec = 0

    for (let j = 0; j < (n * n); j++) {
        exec++
        numexec++

        saida += `${j + 1} `

        if (numexec == (n)) {
            saida += `\n`
            numexec = 0
        }

        if (exec == (n * n))
            break
    }

    return saida
}

console.log(imprime_matrix(3))