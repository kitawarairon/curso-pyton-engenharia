

class Pessoa:
    ''' A tentativa de representar uma pessoa.'''

    def __init__(self, nome, idade, sexo, vivo=True):
        print(f'Construindo nosso objeto: {self}')
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.vivo = vivo

    def descricao(self):
        return f'{self.nome} | {self.idade} | {self.vivo}'
