class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=70):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, o meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe_pai = super().cumprimentar()
        return f'{cumprimentar_da_classe_pai}! Aperto de mão.'


class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    adriano = Mutante(nome='Adriano')
    sergio = Homem(adriano, nome='Sergio')
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
    print(Pessoa.olhos)
    print(sergio.olhos)
    print(adriano.olhos)
    print(id(Pessoa.olhos), id(sergio.olhos), id(adriano.olhos))
    print(Pessoa.metodo_estatico(), sergio.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), sergio.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print((isinstance(adriano, Pessoa)))
    print(isinstance(adriano, Homem))
    print(adriano.olhos)
    print(sergio.cumprimentar())
    print(adriano.cumprimentar())
