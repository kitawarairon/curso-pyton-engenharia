

class Cachorro:
    ''' Essa classe representa um cachorro'''

    def __init__(self, nome, idade, raca, vivo=True):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.vivo = vivo

    def sentar(self):
        ''' Esse método faz com o que o o cachorro sente'''
        print(f'{self.nome} está sentando...')


class Gato:

    def __init__(self, nome, idade, raca, vivo=True):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.vivo = vivo

    def pulando(self):
        print(f'{self.nome} está pulando')