const calc = () => {
    var entradas = [
        {
            nome: 'amigo 1',
            dist: 410
        },
        {
            nome: 'amigo 2',
            dist: 12
        },
        {
            nome: 'amigo 3',
            dist: 60
        }
    ]

    const get_tot_dist = () => entradas.reduce((acc, at) => acc += at.dist, 0)

    const media = () => (get_tot_dist() / entradas.length)

    return media().toFixed(1)
}

console.log(calc())