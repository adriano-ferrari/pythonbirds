class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=70):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    adriano = Pessoa(nome='Adriano')
    sergio = Pessoa(adriano, nome='Sergio')
    print(Pessoa.cumprimentar(sergio))
    print(id(sergio))
    print(sergio.cumprimentar())
    print(sergio.nome)
    print(sergio.idade)
    for filho in sergio.filhos:
        print(filho.nome)
    sergio.sobrenome = 'Ferrari'
    del sergio.filhos
    sergio.olhos = 1
    del sergio.olhos
    print(sergio.__dict__)
    print(adriano.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(sergio.olhos)
    print(adriano.olhos)
    print(id(Pessoa.olhos), id(sergio.olhos), id(adriano.olhos))
