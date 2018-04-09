class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=42):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    genilton = Pessoa(nome='Genilton')
    joao = Pessoa(genilton, nome='João')
    print(Pessoa.cumprimentar(genilton))
    print(id(genilton))
    print(genilton.cumprimentar())
    print(genilton.nome)
    print(genilton.idade)
    for filho in joao.filhos:
        print(filho.nome)
    genilton.sobrenome = 'Nascimento'
    del joao.filhos
    genilton.olhos = 1
    del genilton.olhos
    print(genilton.__dict__)
    print(joao.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(joao.olhos)
    print(genilton.olhos)
    print(id(Pessoa.olhos), id(Pessoa.olhos), id(Pessoa.olhos))




