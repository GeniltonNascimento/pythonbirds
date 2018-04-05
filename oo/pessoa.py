class Pessoa:
    def __init__(self, *filhos, nome=None, idade=42):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    joao = Pessoa(nome='Joao')
    genilton  = Pessoa(joao, nome='Genilton')
    print(Pessoa.cumprimentar(genilton))
    print(id(genilton))
    print(genilton.cumprimentar())
    print(genilton.nome)
    print(genilton.idade)
    for filho in joao.filhos:
        print(filho.nome)