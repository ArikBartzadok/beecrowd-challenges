const construtor = ({altura, base}) => {
    const tiangulo = {
        altura: altura,
        base: base,
        getArea: function() {
            return ((this.base * this.altura)/2)
        }
    }

    return tiangulo.getArea()
}

console.log(construtor({altura: 3, base: 4}))